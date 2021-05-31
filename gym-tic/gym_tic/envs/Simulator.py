from gym_tic.envs.specimen_parsers.Configure import configuration as con
import tensorflow_core as tf
import numpy as np
import copy

def simulate(image, action):
    U_shape = (-1, con['vars'],con['vars'],con['conditions']+1, con['operations'])
    B_shape = (-1, con['conditions']+1,con['conditions']+1)
    X_shape = (-1, con['vars'],con['vars'],1, con['operations'])

    U_size = -np.prod(U_shape)
    B_size = -np.prod(B_shape)
    X_size = -np.prod(X_shape)

    U = copy.deepcopy(image[:,0:U_size])
    B = image[:,U_size:U_size+B_size]
    X = image[:,U_size+B_size:U_size+B_size+X_size]
    A = image[:,U_size+B_size+X_size:]

    U = tf.reshape(U,U_shape)
    # B = tf.reshape(B, B_shape)
    X = tf.reshape(X, X_shape)

    if type(action) == int:
        new_slice = U[:,:,:,action,:]
    elif type(action) == tf.python.framework_ops.EagerTensor:
        zeros = tf.zeros((action.shape[0],1),dtype=tf.float32)
        actions = tf.concat((zeros, action),1)
        actions = tf.reshape(actions, (-1, 1, 1, actions.shape[1], 1))
        new_slice = tf.reduce_sum(U*actions,3)

    X += tf.expand_dims(new_slice,3)

    X = tf.reshape(X,(-1, X_size))
    U = tf.reshape(U,(-1, U_size))

    return tf.concat((U,B,X,A),1)


def break_tensors(image):
    U_shape = (-1, con['vars'],con['vars'],con['conditions']+1, con['operations'])
    B_shape = (-1, con['conditions']+1,con['conditions']+1)
    X_shape = (-1, con['vars'],con['vars'],1, con['operations'])

    U_size = -np.prod(U_shape)
    B_size = -np.prod(B_shape)
    X_size = -np.prod(X_shape)

    U = image[:,0:U_size]
    B = image[:,U_size:U_size+B_size]
    X = image[:,U_size+B_size:]

    return {"U":U, "B":B, "X":X}



