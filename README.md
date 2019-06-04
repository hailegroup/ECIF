### Impedance-Fitting ###
This program fits impedance data with equivalent circuit models using a least-sqares fitting method through python. This program will provide fitted variables along with a fitted pattern corresponding with those variables. Additionaly, an error of these fitted variables is provided via a bootstrapping error calculation method.

## Steps to run the program ##
1. Install Python 3.x or greater on your computer.
1. Install all the necessary libraries
1. Download all files here into a file location on your local computer.
1. Format your data into a three column format csv file with frequency in the first column, the real component of impedance in the second column, and the imaginary component of impedance in the third column.
1. Place this file in /main/General_Circuit.
1. In /main/General_Circuit/config.py type the model you want to fit to inside the quotes. Available circuits are: R, RRC, RRCRC, RRCRCRC, RRQ, RRQRQ, and RRQRQRQ.
1. Type in an initial guess for each parameter to be fit inside the brackets.
1. Open a python console.
1. Change your working directory to /main/General_Circuit.
1. Run Fitting.py.

## Running the Example ##

If you ran the script with the default values using the test data you should have the following figures in the fitting result report in your working directory:

![Image of Z vs. theta](https://github.com/aplymill7/Impedance-Fitting/blob/master/docs/images/Bode.png)


