def secant_method(f, x0, x1):
    import time

    steps_taken = 0
    max_iter = 100
    tolerance = 1e-6

    delta = []
    k = []
    tic = time.clock()
    xk = []

    while steps_taken < max_iter and abs(x1-x0) > tolerance:
        x2 = x1 - ((f(x1) * (x1-x0)) / (f(x1) - f(x0)))
        x1 ,x0 = x2, x1

        delta.append(abs(x1-x0))
        k.append(steps_taken)
        xk.append(x2)

        steps_taken += 1

    toc = time.clock()
    t = toc-tic
    return x2, steps_taken, delta, k, xk, t



