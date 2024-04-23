import matplotlib.pyplot as plt
import numpy as np


def gen_chart(fun_og, fun_inter, node, a, b, filename):
    plt.clf()

    plt.axhline(0, color='black')

    length = 0
    start = a - length
    end = b + length

    x = np.arange(start, end, 0.01)

    plt.plot(x, fun_og(x), "b-", label="funkcja oryginalna")
    plt.plot(x, fun_inter(x), "g-", label="funkcja interpolowa")

    plt.plot(node[0], node[1], "ro", label="węzły")

    plt.legend(loc="upper right")

    plt.savefig(filename)