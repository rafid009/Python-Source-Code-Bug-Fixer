from gym.envs.registration import register

# register(id='tic-v0',
#          entry_point='gym_tic.envs:TicEnv',
# )

register(
    id='specimen_env-v0',
    entry_point='gym_tic.envs:SpecimenEnv',
)
