
from scipy.optimize import linear_sum_assignment
import numpy as np

def linear_assignment(cost_matrix):
    x, y = linear_sum_assignment(cost_matrix)
    return np.array(list(zip(x, y)))