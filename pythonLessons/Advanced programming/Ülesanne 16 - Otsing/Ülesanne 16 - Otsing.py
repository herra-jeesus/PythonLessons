"""
Ülesanne 16 - Otsing
Juhend: https://courses.cs.ttu.ee/w/images/2/20/ITI0140_-_2014_Loeng_otsing.pdf
"""
__author__ = "Borka Martin Orlov"
__email__ = "borka.orlov@gmail.com"

import time
from matplotlib import pyplot
from Tund16gen import *

def timeFunc(func, *args):
    start = time.clock()
    func(*args)
    return time.clock() - start

def linear_search(lst, num):
    for item in lst:
        if item == num:
            return True

    return False

def binary_search(lst, num, sort=False):
    """
    Binary search
    """
    if sort:
        lst = sorted(lst)

    imin = 0
    imax = len(lst)-1

    while imax >= imin:
        imid = (imin+imax) // 2

        if lst[imid] == num:
            return True
        elif lst[imid] < num:
            imin = imid + 1
        else:
            imax = imid - 1

    return False

def main():
    linearTimes = []
    binary1Times = []
    binary2Times = []
    ns = [2**i for i in range(1, 13)]

    for n in ns:
        lst, gen = gimme_my_input(n, "blah")
        times = []

        # linear search test
        for i in range(len(lst)):
            times.append(timeFunc(linear_search, lst, next(gen)))

        avg_time = sum(times) / len(times)
        linearTimes.append(avg_time)

        # binary search test 1
        times = []
        sortedList = sorted(lst)

        for i in range(len(lst)):
            times.append(timeFunc(binary_search, sortedList, next(gen)))

        avg_time = sum(times) / len(times)
        binary1Times.append(avg_time)

        # binary search test 2
        times = []

        for i in range(len(lst)):
            times.append(timeFunc(binary_search, lst, next(gen), True))

        avg_time = sum(times) / len(times)
        binary2Times.append(avg_time)

    # print table of results
    print("| algorithm \t| n \t\t| time (s)")
    print()

    # print Linear Search
    for i, n in enumerate(ns):
        if n < 10000:
            print("| {0} \t| {1} \t\t| {2:.8f}".format("Linear", n, linearTimes[i]))
        else:
            print("| {0} \t| {1} \t| {2:.8f}".format("Linear", n, linearTimes[i]))

    print()

    # print Binary Search (presorted)
    for i, n in enumerate(ns):
        if n < 10000:
            print("| {0} | {1} \t\t| {2:.8f}".format("Bin (presort)", n, binary1Times[i]))
        else:
            print("| {0} | {1} \t| {2:.8f}".format("Bin (presort)", n, binary1Times[i]))

    print()

    # print Binary Search (sort)
    for i, n in enumerate(ns):
        if n < 10000:
            print("| {0} \t| {1} \t\t| {2:.8f}".format("Bin (sort)", n, binary2Times[i]))
        else:
            print("| {0} \t| {1} \t| {2:.8f}".format("Bin (sort)", n, binary2Times[i]))

    # plot the times
    subplot = pyplot.subplot()
    subplot.set_xlabel("n")
    subplot.set_xscale("log")
    subplot.set_ylabel("Time (s)")
    subplot.set_yscale("log")
    subplot.plot(ns, linearTimes, "r", label="Linear Search")
    subplot.plot(ns, binary1Times, "g", label="Binary Search (presorted)")
    subplot.plot(ns, binary2Times, "b", label="Binary Search (sort)")
    subplot.legend(loc="upper left", shadow=True);
    pyplot.show()

if __name__ == "__main__":
    main()