#!/usr/bin/python
# -*- coding: utf-8 -*-

#Import Packages to be used in the file
import numpy
import Fitting as fit
import statistics
import pandas as pd
import matplotlib.pyplot as plt

def strap(residuals, FArr, ZArr, params, ParamNames):

#Break apart complex array of original residuals
 length=int(len(residuals)/2)
 Real_residuals = residuals[0:length]
 Imag_residuals = residuals[length:]
 
 #Break apart original complex array
 RArr = ZArr.real
 ImArr = ZArr.imag
  
#Obtain the Statistical parameters of the Residuals from original fitting (Needed input = Real + Imaginary Residuals)
 Real_res_error = statistics.stdev(Real_residuals)
 Imag_res_error = statistics.stdev(Imag_residuals)
 Real_res_mean = statistics.mean(Real_residuals)
 Imag_res_mean = statistics.mean(Imag_residuals)
 
#Initialize iterator
 i=0

#Initilize Matrix to carry disributions of fitted variables
 Fitted_Variables_Matrix = []
 
 #Initialize Parameters list
 global Param_names

#Main Bootstrap. Fitting to be performed x times in i<x
 while i<50:
    #Generate a new set of residuals based on the statistics acquired above. 
    Boot_R_residuals = numpy.random.normal(Real_res_mean,Real_res_error,size=length)
    Boot_i_residuals = numpy.random.normal(Imag_res_mean,Imag_res_error, size=length)
    #Generate a new data set based on these residuals (Requires original impedance data)
    new_r_boot = RArr + Boot_R_residuals
    new_i_boot = ImArr + Boot_i_residuals
    total_boot = new_r_boot + 1j*new_i_boot
    
    #Check simulated impedance (uncomment to check boots)
    #plt.plot(new_r_boot, -new_i_boot)
    #plt.savefig("boots.png")
    
    #Perform a fit on newly generated data (Requires parameter guesss)
    fit_result, pn = fit.custom_fitting(FArr, total_boot, params)
    #Generate a list of variables from fit
    Fitted_variables = list(fit_result.x)
    
    Fitted_Variables_Matrix.append(Fitted_variables)
    
    i=i+1
    
    Param_names = pn

 Fitted_Variables_Matrix = pd.DataFrame(Fitted_Variables_Matrix, columns=ParamNames)
 Correlation_Matrix = Fitted_Variables_Matrix.corr()
   
#Take the standard deviation of each of the fitted variables distributions    
 Stds = Fitted_Variables_Matrix.std(axis=0)

#Take the average fit
 means = Fitted_Variables_Matrix.mean(axis=0)

#Compile all of the fitted variables errors into a single list
 evz=list(Stds)
 ms=list(means)


#Compile and save these results to a csv 
 Params=list(zip(Param_names, ms, evz))
 Paramsdf =pd.DataFrame(data = Params, columns=['Parameters', 'Value', 'Error'])
 Paramsdf.to_csv('Fitted_Parameters.csv', index=False)
 
 #Clear figure at end of program
 plt.clf()
 
 #Return Fitted Params
 return ms, Correlation_Matrix

