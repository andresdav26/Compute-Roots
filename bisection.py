def bisection_method(f, a, b):

    import numpy as np
    import time

    steps_taken = 0
    tolerance = 1e-6
    max_iter = 50

    delta = []
    k = []
    tic = time.clock()
    xk = []
#    m = 1

    while abs(b-a) > tolerance and steps_taken < max_iter:
        m = a+((b-a)/2.0)

        if f(m) > 0:
            b = m
        else:
            a = m

        delta.append(abs(b-a))
        xk.append(m)
        k.append(steps_taken)

        steps_taken += 1

    root = a+((b-a)/2.0)
    toc = time.clock()
    t = toc-tic

    return root, steps_taken, delta, k, xk, t


