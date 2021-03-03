import numpy as np
import matplotlib.pylab as plt

def step_function_old(x):
    y = x > 0
    return y.astype(np.int)

def step_function(x):
    return np.array(x>0, dtype=np.int)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def relu(x):
    return np.maximum(0, x)

if __name__ == '__main__':
    x = np.arange(-5.0, 5.0, 0.1)
    y = relu(x)
    plt.ylim(-0.1,2.1)
    plt.plot(x, y)
    plt.show()