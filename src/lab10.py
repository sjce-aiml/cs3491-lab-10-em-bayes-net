"""Lab 10 starter code: EM for a Bayesian network with a hidden variable.

Network: Coin (hidden, A or B, prior 0.5) -> each of n tosses (Heads ~ Bernoulli(theta_coin)).
Each trial records only the number of heads out of n tosses.
"""
import numpy as np

def em_two_coins(heads, n, theta_a=0.6, theta_b=0.5, iters=10):
    """Return (theta_a, theta_b) after `iters` EM iterations."""
    raise NotImplementedError('TODO: implement this')

def log_likelihood(heads, n, theta_a, theta_b):
    raise NotImplementedError('TODO: implement this')
