import numpy

#This function takes inputs equivalent circuit model parameters, a frequency array, and the name of the model considered
#and returns the the impedance ouput given these parameters, as well as the bounds to be considered when refining on them.


class circuit_output:
    def __init__(self, z=[], low_bound=[], high_bound=[], parameters_names=[]):
        self.z = z
        self.low_bound = low_bound
        self.high_bound = high_bound
        self.parameters_names = parameters_names

def Z(parameters, x, modelname):
    
    x = numpy.array(x)
    
    if (modelname == 'R'):
        a = parameters
        z = a
        low_bound = [0.0]
        high_bound = [numpy.inf]
        parameters_names = ['R0']
    
    elif (modelname == 'RRC'):
        a, b, c = parameters
        z = a +1/(1/b+c*(1j*2*3.14159*x))
        low_bound = [0.0, 0.0, 0.0]
        high_bound = [numpy.inf, numpy.inf, numpy.inf]
        parameters_names = ['R0', 'R1', 'C1']
    
    elif (modelname == 'RRQ'):
        a, b, c, d = parameters
        z = a +1/(1/b+c*(1j*2*3.14159*x)**d)
        low_bound = [0.0, 0.0, 0.0, 0.0]
        high_bound = [numpy.inf, numpy.inf, numpy.inf, 1.0]
        parameters_names = ['R0', 'R1', 'Q1', 'Alpha1']

 
    elif (modelname == 'RRCRC'):
        
        a, b, c, d, e = parameters
        z = a+1/(1/b+c*(1j*2*3.14159*x))+1/(1/d+e*(1j*2*3.14159*x))
        low_bound = [0.0, 0.0, 0.0, 0.0, 0.0]
        high_bound = [numpy.inf, numpy.inf, numpy.inf, numpy.inf, numpy.inf]
        parameters_names = ['R0', 'R1', 'C1', 'R2', 'C2']

    elif (modelname == 'RRQRQ'):
        
        a, b, c, d, e, f, g = parameters
        z = a+1/(1/b+c*(1j*2*3.14159*x)**d)+1/(1/e+f*(1j*2*3.14159*x)**g)
        low_bound = [0.0, 0.0, 0.0, 0.0, 0.0 , 0.0 , 0.0]
        high_bound = [numpy.inf, numpy.inf, numpy.inf, 1.0, numpy.inf, numpy.inf, 1.0]
        parameters_names = ['R0', 'R1', 'Q1', 'Alpha1', 'R2', 'Q2', 'Alpha2']
    
    else:
        print('Invalid modelname provided')

    return circuit_output(z, low_bound, high_bound, parameters_names)
