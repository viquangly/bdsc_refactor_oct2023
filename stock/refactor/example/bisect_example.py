
import bisect


def slow_search(x):
    if 0.10 < x <= 0.20:
        return 0.05

    elif 0.20 < x <= 0.30:
        return 0.06

    elif 0.30 < x <= 0.40:
        return 0.07

    elif 0.40 < x <= 0.50:
        return 0.08

    elif 0.50 < x <= 0.60:
        return 0.09

    elif 0.60 < x <= 0.70:
        return 0.10

    elif 0.70 < x <= 0.80:
        return 0.11

    else:
        return 0.15


def loop_search(x):
    sequence = (.2, .3, .4, .5, .6, .7, .8)
    response = (.05, .06, .07, .08, .09, .1, .11)
    for threshold, value in zip(sequence, response):
        if x <= threshold:
            return value
    return 0.15


def fast_search(x):
    sequence = (.2, .3, .4, .5, .6, .7, .8)
    response = (.05, .06, .07, .08, .09, .1, .11)
    if x > sequence[-1]:
        return 0.15
    index = bisect.bisect_left(sequence, x)
    return response[index]


if __name__ == '__main__':

    %%timeit
    slow_search(.79)

    %%timeit
    loop_search(.79)

    %%timeit
    fast_search(.79)