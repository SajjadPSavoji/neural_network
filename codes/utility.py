import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
def alphabetize(x,y):
    if x.get_name()>y.get_name():
        return 1
    return -1

def abs_mean(values):
    """Compute the mean of the absolute values a set of numbers.
    For computing the stopping condition for training neural nets"""
    return np.mean(np.abs(values))

# @implimente:----------------------------------
def plot_decision_boundary(network, xmin=-1 , xmax=1 , ymin=-1 , ymax=1 , step = 0.05):
    '''
    input:  neural network
            xmin , xmax , ymin , ymax (asumming that the dimension of feature vector is 2)
    '''
    X , Y = np.meshgrid(np.arange(xmin , xmax , step) , np.arange(ymin , ymax , step))
    for xi , yi in tqdm(zip(X.flat, Y.flat) , "decision surface:"):
        # print(X)
        # print("------------")
        # print(Y)
        network.clear_cache()
        network.inputs[0].set_value(xi)
        network.inputs[1].set_value(yi)
        o = network.output.output()
        # print(type(o))
        # print(o)
        if o > 0.5 :
            plt.scatter(xi , yi , c='r')
        else:
            plt.scatter(xi , yi , c='b')
    plt.title("decision boundries of network")
    plt.show()
# @end:----------------------------------------- 
