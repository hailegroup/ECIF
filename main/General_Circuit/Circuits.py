import numpy

#This function takes inputs equivalent circuit model parameters, a frequency array, and the name of the model considered
#and returns the the impedance ouput given these parameters, as well as the bounds to be considered when refining on them.

def Z(parameters, x, modelname):
    
    x = numpy.array(x)
    
    if (modelname == 'R'):
        a = parameters
        result = a
        return result, [0.0], [numpy.inf], ['R0']
    
    elif (modelname == 'RRC'):
        a, b, c = parameters
        result = a +1/(1/b+c*(1j*2*3.14159*x))
        return result, [0.0, 0.0, 0.0], [numpy.inf, numpy.inf, numpy.inf], ['R0', 'R1', 'C1']
    
    elif (modelname == 'RRQ'):
        a, b, c, d = parameters
        result = a +1/(1/b+c*(1j*2*3.14159*x)**d)
        return result, [0.0, 0.0, 0.0, 0.0], [numpy.inf, numpy.inf, numpy.inf, 1.0], ['R0', 'R1', 'Q1', 'Alpha1']
 
    elif (modelname == 'RRCRC'):
        
        a, b, c, d, e = parameters
        result = a+1/(1/b+c*(1j*2*3.14159*x))+1/(1/d+e*(1j*2*3.14159*x))
        return result, [0.0, 0.0, 0.0, 0.0, 0.0], [numpy.inf, numpy.inf, numpy.inf, numpy.inf, numpy.inf], ['R0', 'R1', 'C1', 'R2', 'C2']

    elif (modelname == 'RRQRQ'):
        
        a, b, c, d, e, f, g = parameters
        result = a+1/(1/b+c*(1j*2*3.14159*x)**d)+1/(1/e+f*(1j*2*3.14159*x)**g)
        return result, [0.0, 0.0, 0.0, 0.0, 0.0 , 0.0 , 0.0], [numpy.inf, numpy.inf, numpy.inf, 1.0, numpy.inf, numpy.inf, 1.0], ['R0', 'R1', 'Q1', 'Alpha1', 'R2', 'Q2', 'Alpha2']
    
    else:
        print('Invalid modelname provided')
