"""
Tasks for module 4
"""

#A8
from random import gauss

def samples(n, mu):
    # returns a list of n random values from a normal distribution with a mean mu
    # do not modify
    return [gauss(mu, 10) for _ in range(n)]

# work here
def gauss_test(n, mus):
    pass

#B4
def approximate_all_poker_frequencies(n, n_processes):
    pass

if __name__ == '__main__':
    print("A8:")
    print(gauss_test(10000, [-3, 10, 2.3]))
    print("B4:")
    approximate_all_poker_frequencies(10000, 4)