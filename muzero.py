from configs.config import MuZeroConfig, make_config, playtest_config
from shared_storage.shared_storage import SharedStorage
from search.self_play import run_selfplay, run_eval, play_game
from training.replay_buffer import ReplayBuffer
from training.training import train_network
# from graphMaker import graphMakingFunction
import os
import pickle
import json
from configs.Configure import configuration as con
import logging
import torch

torch.cuda.device(torch.device('cuda:1'))
def save_all_networks(storage, save_path):
    default_network = storage.latest_network()
    default_network.save_networks(save_path)
    with open(os.path.join(save_path, 'optimizer.pkl'), 'wb') as g:
        pickle.dump(storage.optimizer_info, g)


def muzero(config: MuZeroConfig, test_config: MuZeroConfig, save_path, load=False):
    """
    MuZero training is split into two independent parts: Network training and
    self-play data generation.
    These two parts only communicate by transferring the latest networks checkpoint
    from the training to the self-play, and the finished games from the self-play
    to the training.
    In contrast to the original MuZero algorithm this version doesn't works with
    multiple threads, therefore the training and self-play is done alternately.
    """

    replay_buffer = ReplayBuffer(config)

    storage = SharedStorage(config.new_network(), config.uniform_network(), config.new_optimizer())
    storage.record_this = False
    for loop in range(config.nb_training_loop):
        print("Training loop", loop)
        logging.info("loop: "+str(loop))

        #Record every few loops as specified at con['record_every'] or at the last loop
        if (loop%con['record_every']==0 and loop !=0) or loop==con['loops']:
            # storage.record_this = True
            save_all_networks(storage, save_path)
        storage.latest_network().train()
        score_train, _ = run_selfplay(config, storage, replay_buffer, config.nb_episodes, render=False)
        storage.current_network.train()
        train_network(config, storage, replay_buffer, config.nb_epochs, loop)

        print("Train score:", score_train)
        storage.latest_network().eval()
        storage.current_network.eval()
        eval_score, game_sorts, stats  = run_eval(test_config, storage, con['EVAL_GAMES'])

        print("Eval score:", eval_score)
        logging.info(eval_score)
        print(f"MuZero played {config.nb_episodes * (loop + 1)} "
              f"episodes and trained for {config.nb_epochs * (loop + 1)} epochs.\n")
    print("Training finished")

    save_all_networks(storage, save_path)

    return storage

def play_test(network):
    """Evaluate MuZero without noise added to the prior of the root and without softmax action selection"""
    config = playtest_config()
    play_game(config, network.latest_network(), train=False, render_this=True)

def get_weight_path():
    weight_path = con['save_path']
    if not os.path.exists(weight_path):
        os.makedirs(weight_path)
    models = [item for item in os.listdir(weight_path) if 'model' in item]

    next_model = "model "+str(len(models))
    weight_path = os.path.join(weight_path, next_model)
    os.makedirs(weight_path)
    return weight_path

def save_model_stats(weight_path, stats):
    results_path = os.path.join(weight_path, "results.txt")
    config_path = os.path.join(weight_path, "config.json")

    with open(results_path,'w') as g:
        g.write(str(stats))

    with open(config_path,'w') as g:
        json.dump(con,g)


# def make_graphs(path, game_sorts):
#         SUCCESSES = os.path.join(path, "success_graphs")
#         FAILURES = os.path.join(path, "failure_graphs")
#         if not os.path.exists(SUCESSES):
#             os.mkdir(SUCCESSES)
#         if not os.path.exists(FAILURES):
#             os.mkdir(FAILURES)

#         for game in game_sorts:
#             file = game[0]
#             score = game[1]

#             if score ==1:
#                 out_path = SUCCESSES
#             else:
#                 out_path = FAILURES

#             in_path = os.path.join(con['specimen_eval_path'],file)
#             answers_path = in_path.replace(".py","_answers.txt")
#             with open(answers_path, 'r') as f:
#                 answers = f.read()
#             answers = [int(x) for x in answers.split("]")[0].replace("[",'').split(",")]

#             graphMakingFunction(in_path, out_path, answers)





if __name__ == '__main__':
    config = make_config()
    test_config = playtest_config()
    weight_path = get_weight_path()
    logging.basicConfig(filename=os.path.join(weight_path,'log'), level=logging.INFO)
    storage = muzero(config, test_config,weight_path,load=False)
    for i in range(100):
        final_eval, game_sorts, stats = run_eval(test_config, storage, con['final_eval'], plot=True, weight_path=weight_path)
        sort_file = os.path.join(weight_path, "game_sort.txt")
        with open(sort_file, 'a+') as g:
            g.write(str(game_sorts))

    print("Final Eval: ",final_eval,stats)
    save_model_stats(weight_path,stats)

    #TODO Set up visualizer install
    # if con['generate_graphs']:
    #     make_graphs(weight_path, game_sorts)

    print("Done")


