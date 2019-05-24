
def Z(parameters, x, modelname):
    if (modelname == 'RRQRQ')
        a, b, c, d, e, f, g, = parameters
        return a + 1 / (1 / b + c * (1j * 2 * 3.14159 * x) ** d) + 1 / (1 / e + f * (1j * 2 * 3.14159 * x) ** g), [0.0, 0.0, 0.0, 0.0, 0.0 , 0.0 , 0.0], [numpy.inf, numpy.inf, numpy.inf, 1.0, numpy.inf, numpy.inf, 1.0]
    else
        print('Invalid modelname provided')
