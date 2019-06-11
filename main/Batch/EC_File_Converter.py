### This Script Extracts Impedance Data from an Ec_Lab ouput .mpt to and creates a corresponding csv file ###

#For command line commands
import os

#For data handling
import pandas as pd

#For working with strings
import re

#Get the files to be measured
HomeFiles=os.listdir()
ImpedanceFiles = []

pattern = re.compile(".mpt$")  # Compile a regex
for line in HomeFiles:
    if pattern.search(line) != None:      # If a match is found 
        ImpedanceFiles.append(line)

for line in ImpedanceFiles:
    file=open(line, 'r', encoding='cp1252')
    F = []
    R  = []
    Im = []

    for thing in file.readlines()[60:]:
        fields = thing.split()
        if float(fields[2])>=0:
            F = F + [float(fields[0])]
            R = R + [float(fields[1])]
            Im = Im + [-float(fields[2])]
    file.close()
    
    EISdata=list(zip(F, R, Im))
    df = pd.DataFrame(data = EISdata, columns=['Frequency', 'R(ohmcm^2)','Im(ohmcm^2)'])
    namesplit = line.split(".")
    outfilename = namesplit[0] + ".csv" 
    df.to_csv(outfilename,index=False,header=True)
