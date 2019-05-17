#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy
import fitting_IM as fit
import statistics
import pandas as pd

Real_res_error = statistics.stdev(Real_residuals)
Imag_res_error = statistics.stdev(Imag_residuals)
Real_res_mean = statistics.mean(Real_residuals)
Imag_res_mean = statistics.mean(Imag_residuals)
    
i=0
v1 = list()
v2 = list()
v3 = list()
v4 = list()
v5 = list()
v6 = list()
v7 = list()

while i<100:
    Boot_R_residuals = numpy.random.normal(Real_res_mean,Real_res_error,size=reals_length)
    Boot_i_residuals = numpy.random.normal(Imag_res_mean,Imag_res_error, size=reals_length)
    new_r_boot = RArr + Boot_R_residuals
    new_i_boot = ImArr + Boot_i_residuals
    total_boot = new_r_boot + new_i_boot
    fit_result = fit.custom_fitting(F, total_boot, params)
    Fitted_variables = list(fit_result.x)

    a = Fitted_variables[0]
    b = Fitted_variables[1]
    c = Fitted_variables[2]
    d = Fitted_variables[3]
    e = Fitted_variables[4]
    f = Fitted_variables[5]
    g = Fitted_variables[6]

    v1.append(a)
    v2.append(b)
    v3.append(c)
    v4.append(d)
    v5.append(e)
    v6.append(f)
    v7.append(g)
    i=i+1
   
    
ev1=statistics.stdev(v1)
ev2=statistics.stdev(v2)
ev3=statistics.stdev(v3)
ev4=statistics.stdev(v4)
ev5=statistics.stdev(v5)
ev6=statistics.stdev(v6)
ev7=statistics.stdev(v7)
  
evz=[]
evz.append(ev1)
vz.append(ev2)
evz.append(ev3)
evz.append(ev4)
evz.append(ev5)
evz.append(ev6)
evz.append(ev7)
        
################################################################
    
Params=list(zip(First_Fit, evz, ParamNames))
Paramsdf =pd.DataFrame(data = Params, columns=['Value', 'Error', 'Parameter'])
Paramsdf.to_csv('fit_params_'+outfilename)
