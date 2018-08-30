def IQI(f, x0, x1, x2):
    import time

    max_iter = 50
    tolerance = 1e-6
    steps_taken = 0

    delta = []
    k = []
    tic = time.clock()
    xk = []


    while steps_taken < max_iter and abs(x1-x0) > tolerance:
        fx0 = f(x0)
        fx1 = f(x1)
        fx2 = f(x2)
        L0 = (x0 * fx1 * fx2) / ((fx0 - fx1) * (fx0 - fx2))
        L1 = (x1 * fx0 * fx2) / ((fx1 - fx0) * (fx1 - fx2))
        L2 = (x2 * fx1 * fx0) / ((fx2 - fx0) * (fx2 - fx1))
        new = L0 + L1 + L2

        delta.append(abs(x1-x0))
        k.append(steps_taken)
        xk.append(new)

        x0, x1, x2 = new, x0, x1
        steps_taken += 1
    toc = time.clock()
    t = toc-tic
    return x0, steps_taken, delta, k, xk, t

