#!/usr/bin/python
# -*- coding: utf-8 -*-

#Import Packages to be used in the file
import numpy
import Fitting as fit
import statistics
import pandas as pd
import matplotlib.pyplot as plt

def strap(residuals, FArr, ZArr, params):

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

#Initialize list to carry distributions of fitted variables
 v1 = list()
 v2 = list()
 v3 = list()
 v4 = list()
 v5 = list()
 v6 = list()
 v7 = list()
 
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
    
    #Pull out these variables from the list
    a = Fitted_variables[0]
    b = Fitted_variables[1]
    c = Fitted_variables[2]
    d = Fitted_variables[3]
    e = Fitted_variables[4]
    f = Fitted_variables[5]
    g = Fitted_variables[6]
    
    #Start adding these fitted variables to distributions of each one
    v1.append(a)
    v2.append(b)
    v3.append(c)
    v4.append(d)
    v5.append(e)
    v6.append(f)
    v7.append(g)
    i=i+1
    
    Param_names = pn
   
#Take the standard deviation of each of the fitted variables distributions    
 ev1=statistics.stdev(v1)
 ev2=statistics.stdev(v2)
 ev3=statistics.stdev(v3)
 ev4=statistics.stdev(v4)
 ev5=statistics.stdev(v5)
 ev6=statistics.stdev(v6)
 ev7=statistics.stdev(v7)

#Take the average fit
 m1=statistics.mean(v1)
 m2=statistics.mean(v2)
 m3=statistics.mean(v3)
 m4=statistics.mean(v4)
 m5=statistics.mean(v5)
 m6=statistics.mean(v6)
 m7=statistics.mean(v7)

#Compile all of the fitted variables errors into a single list
 evz=[]
 evz.append(ev1)
 evz.append(ev2)
 evz.append(ev3)
 evz.append(ev4)
 evz.append(ev5)
 evz.append(ev6)
 evz.append(ev7)

 ms=[]
 ms.append(m1)
 ms.append(m2)
 ms.append(m3)
 ms.append(m4)
 ms.append(m5)
 ms.append(m6)
 ms.append(m7)

#Compile and save these results to a csv 
 Params=list(zip(Param_names, ms, evz))
 Paramsdf =pd.DataFrame(data = Params, columns=['Parameters', 'Value', 'Error'])
 Paramsdf.to_csv('Fitted_Parameters.csv', index=False)
 
 #Clear figure at end of program
 plt.clf()
 
 #Return Fitted Params
 return ms
