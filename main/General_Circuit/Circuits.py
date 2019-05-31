import numpy

def Z(parameters, x, modelname):
    
    x = numpy.array(x)
    
    if (modelname == 'R'):
        a = parameters
        result = a
        return result, [0.0], [numpy.inf]
    
    elif (modelname == 'RRQ'):
        a, b, c, d = parameters
        result = a +1/(1/b+c*(1j*2*3.14159*x)**d)
        return result, [0.0, 0.0, 0.0, 0.0], [numpy.inf, numpy.inf, numpy.inf, 1.0]
    
    elif (modelname == 'RRQRQ'):
        
        a, b, c, d, e, f, g, = parameters
        result = a+1/(1/b+c*(1j*2*3.14159*x)**d)+1/(1/e+f*(1j*2*3.14159*x)**g)
        return result, [0.0, 0.0, 0.0, 0.0, 0.0 , 0.0 , 0.0], [numpy.inf, numpy.inf, numpy.inf, 1.0, numpy.inf, numpy.inf, 1.0]
    
    else:
        print('Invalid modelname provided')
