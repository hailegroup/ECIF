# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 12:09:59 2019

@author: Austin
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

def Impedance(x, a, b, c, d):
        x=np.array(x)
        z = a +1/(1/b+c*(1j*2*3.14159*x)**d)
        Real=z.real
        Imag=z.imag
        Mod = np.sqrt(Real ** 2 + Imag ** 2)
#        NegImag=-z.imag
        
        return Mod

axis_color = 'lightblue'

fig = plt.figure()
ax = fig.add_subplot(111)

# Adjust the subplots region to leave some space for the sliders and buttons
fig.subplots_adjust(left=0.25, bottom=0.25)

x = np.logspace(-1, 6, 50)
R0 = 1
R1 = 1
Q1 = 0.01
Alpha1 = 1

# Draw the initial plot
# The 'line' variable is used for modifying the line later
[line] = ax.plot(x, Impedance(x, R0, R1, Q1, Alpha1), linewidth=2, color='red')
ax.set_xscale('log')
ax.set_xlim([0.1, 1000000])
ax.xaxis.tick_top()
ax.set_ylim([0, 5])
ax.set_xlabel(xlabel='Frequency(Hz)', position = (0.5, 10))
ax.set_ylabel(ylabel='|Z| (ohm)')

# Add two sliders for tweaking the parameters

# Define an axes area and draw a slider in it
R0_slider_ax  = fig.add_axes([0.25, 0.15, 0.65, 0.03], axisbg=axis_color)
R0_slider = Slider(R0_slider_ax, 'R0', 0.0, 2.5, valinit=R0)

R1_slider_ax  = fig.add_axes([0.25, 0.10, 0.65, 0.03], axisbg=axis_color)
R1_slider = Slider(R1_slider_ax, 'R1', 0.0, 2.5, valinit=R1)

Q1_slider_ax  = fig.add_axes([0.25, 0.05, 0.65, 0.03], axisbg=axis_color)
Q1_slider = Slider(Q1_slider_ax, 'Q1', -7 , -1, valinit=Q1)

A1_slider_ax  = fig.add_axes([0.25, 0.00, 0.65, 0.03], axisbg=axis_color)
A1_slider = Slider(A1_slider_ax, 'Alpha1', 0.0, 1.0, valinit=Alpha1)

# Define an action for modifying the line when any slider's value changes
def sliders_on_changed(val):
    line.set_ydata(Impedance(x, R0_slider.val, R1_slider.val, 10**(Q1_slider.val), A1_slider.val))
    fig.canvas.draw_idle()
R0_slider.on_changed(sliders_on_changed)
R1_slider.on_changed(sliders_on_changed)
Q1_slider.on_changed(sliders_on_changed)
A1_slider.on_changed(sliders_on_changed)

# Add a button for resetting the parameters
reset_button_ax = fig.add_axes([0.01, 0.025, 0.1, 0.04])
reset_button = Button(reset_button_ax, 'Reset', color=axis_color, hovercolor='0.975')
def reset_button_on_clicked(mouse_event):
    R0_slider.reset()
    R1_slider.reset()
    Q1_slider.reset()
    A1_slider.reset()
reset_button.on_clicked(reset_button_on_clicked)

# Add a set of radio buttons for changing color
color_radios_ax = fig.add_axes([0.025, 0.5, 0.15, 0.15], axisbg=axis_color)
color_radios = RadioButtons(color_radios_ax, ('red', 'blue', 'green'), active=0)
def color_radios_on_clicked(label):
    line.set_color(label)
    fig.canvas.draw_idle()
color_radios.on_clicked(color_radios_on_clicked)

plt.show()
