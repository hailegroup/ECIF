import numpy
from scipy.optimize import least_squares
import Circuits as cir
import config

#Get the type of circuit from the config file
modelname = config.Circuit_Type

# define impedance model
def model(parameters, x, modelname):
    result, bound = cir.Z(parameters, x, modelname)

# define residual function for fitting
def res_vec(parameters, x, y):
    y_cal, bounds = model(parameters, x, modelname)
    z = y-y_cal
    modulus = numpy.sqrt(y_cal.real ** 2 + y_cal.imag ** 2)
    a = z.real/modulus
    b = z.imag/modulus
    z = a.tolist()+b.tolist()
    return numpy.array(z)


# least-square fitting
def custom_fitting(freq, data, parameters):
    x_data = numpy.array(freq)
    y_data = numpy.array(data)
    parameters = numpy.array(parameters)
    fitting_result = least_squares(res_vec,parameters,bounds, args=(x_data, y_data))
    return fitting_result
