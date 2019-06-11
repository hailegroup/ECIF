import numpy
from scipy.optimize import least_squares
import Circuits as cir
import config

#Get the type of circuit from the config file
modelname = config.Circuit_Type

# define residual function for fitting
def res_vec(parameters, x, y):
    result= cir.Z(parameters, x, modelname)
    As_recieved = result.z
    z = y-As_recieved
    modulus = numpy.sqrt(As_recieved.real ** 2 + As_recieved.imag ** 2)
    a = z.real/modulus
    b = z.imag/modulus
    z = a.tolist()+b.tolist()
    return numpy.array(z)


# least-square fitting
def custom_fitting(freq, data, parameters):
    result= cir.Z(parameters, freq, modelname)
    x_data = numpy.array(freq)
    y_data = numpy.array(data)
    parameters = numpy.array(parameters)
    fitting_result = least_squares(res_vec,parameters,bounds=(result.low_bound,result.high_bound), args=(x_data, y_data))
    return fitting_result, result.parameters_names
