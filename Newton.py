def appr_taylor(f, x):
    h = 1e-6
    return (f(x+h) - f(x)) / h



def newton_method(f, x ):
    import time
    steps_taken = 0
    tolerance = 1e-6
    max_iter = 50

    delta = []
    k = []
    tic = time.clock()
    xk = []
    h = 1
    while abs(h) > tolerance and steps_taken < max_iter:
        df = appr_taylor(f, x)
        h = -f(x)/df
        x = x + h

        delta.append(abs(h))
        k.append(steps_taken)
        xk.append(x)

        steps_taken += 1

    toc = time.clock()
    t = toc-tic
    return x, steps_taken,delta,k,xk,t


