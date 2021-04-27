import matplotlib.pyplot as plt
from random import random
import math

def genreate_pareto(a,b,y):
    x = b/(1 - y)**(1/a)
    return x

if __name__ == "__main__":
    a = 1
    b = 1
    bins = 100
    counts = 100
    results = []
    for i in range(counts):
        rand = random()
        if rand == 0:
            i -= 1
        else:
            res = genreate_pareto(a, b, rand)
            results.append(res)
    plt.hist(results, bins=bins)
    plt.savefig("images/pareto.png")
    plt.show()
