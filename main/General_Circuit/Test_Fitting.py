# -*- coding: utf-8 -*-

#Import the necessary libraries
import numpy
import Fitting as fit
import Bootstrap as boot
import matplotlib.pyplot as plt
import statistics
import config

#Acquire user input from config file
modelname = config.Circuit_Type
params = config.Initial_Parameters

#Open test file
file=open('test.csv', 'r', encoding='cp1252')

#Initialize lists
F=[]
R=[]
Im=[]

#Read in the file
for line in file.readlines()[1:]:
    fields=line.split(',')
    F=F+[float(fields[0])]
    R=R+[float(fields[1])]
    Im=Im+[float(fields[2])]

#Form data into complex array
FArr=numpy.array(F)
RArr=numpy.array(R)
ImArr=-numpy.array(Im)*1j
TotArr=RArr+ImArr

#Fit the data
fit_result = fit.custom_fitting(F, TotArr, params, modelname)
Fitted_variables = fit_result.x

#Obtain the residuals
residuals = fit.res_vec( Fitted_variables, FArr, TotArr)

#Bootstrap to get error and generate final model
boot_params = boot.strap(residuals, FArr, TotArr, Fitted_variables)
boot_generation = fit.model(boot_params, FArr)
Real_Boot_Fit = boot_generation.real
Imag_Boot_Fit = boot_generation.imag

#Nyquist Plot
plt.plot(Real_Boot_Fit, -Imag_Boot_Fit, label = 'Boot Fit')
plt.plot(R, Im, label = 'Measured')

