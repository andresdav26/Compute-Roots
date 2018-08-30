def brents_method(f, x0, x1):
    import time

    max_iter = 50
    tolerance = 1e-6
    steps_taken = 0

    delta = []
    k = []
    tic = time.clock()
    xk = []


    fx0 = f(x0)
    fx1 = f(x1)

    assert (fx0 * fx1) <= 0, "Root not bracketed" 

    if abs(fx0) < abs(fx1):
        x0, x1 = x1, x0
        fx0, fx1 = fx1, fx0
        x2, f2 = x0, fx0


    while steps_taken < max_iter and abs(x1-x0) > tolerance:
        fx0 = f(x0)
        fx1 = f(x1)
        fx2 = f(x2)

        if fx0 != fx2 and fx1 != fx2:
            L0 = (x0 * fx1 * fx2) / ((fx0 - fx1) * (fx0 - fx2))
            L1 = (x1 * fx0 * fx2) / ((fx1 - fx0) * (fx1 - fx2))
            L2 = (x2 * fx1 * fx0) / ((fx2 - fx0) * (fx2 - fx1))
            new = L0 + L1 + L2

        else:
            new = x1 - ( (fx1 * (x1 - x0)) / (fx1 - fx0) )


        delta.append(abs(x1-x0))
        k.append(steps_taken)
        xk.append(new)

        fnew = f(new)
        d, x2 = x2, x1

        if (fx0 * fnew) < 0:
            x1 = new
        else:
            x0 = new

        if abs(fx0) < abs(fx1):
            x0, x1 = x1, x0

        steps_taken += 1
    toc = time.clock()
    t = toc-tic
    return x1, steps_taken, delta, k, xk, t


