import numpy
from scipy.optimize import least_squares


# define impedance model
def model(parameters, x):
    a, b, c, d, e, f, g = parameters
    return a + 1 / (1 / b + c * (1j * 2 * 3.14159 * x) ** d) + 1 / (1 / e + f * (1j * 2 * 3.14159 * x) ** g)


# define lower and upper bound for parameters
def bound():
    return [0.0, 0.0, 0.0, 0.0, 0.0 , 0.0 , 0.0], [numpy.inf, numpy.inf, numpy.inf, 1.0, numpy.inf, numpy.inf, 1.0]


# define residual function for fitting
def res_vec(parameters, x, y):
    y_cal = model(parameters, x)
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
    fitting_result = least_squares(res_vec,parameters,bounds=(bound()), args=(x_data, y_data))
    return fitting_result
