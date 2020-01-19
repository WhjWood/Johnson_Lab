import numpy as np
import math, os
import pandas as pd

#WhjWood 19/01/2020

# This script calculates the full width at half maximum of grana from SIM images of chloroplasts
# using the same method as in Wood & Barnett et al. (2019)

# FOLDER : the path to the folder where all the cross sections files are saved
# Note. the folder should contain files of grana cross sections and nothing else.
FOLDER = r"./test_grana_cross_sections"

results = []
for filename in os.listdir(FOLDER):
    data = pd.read_csv(FOLDER+"/"+filename)
    data["Y"]=data["Y"]-data["Y"].min()
    dX=data["X"][1]-data["X"][0]
    FWHM = len(data['Y'][data['Y']>=0.5*data['Y'].max()])*dX
    results.append(FWHM)
    


# results_name : path to file where you want to save the results saved
# note. if the file already exists it will be overwritten!
results_name = r"../test_cross_sections.txt"
results_file = open(results_name,'w')
for r in results:
    results_file.write(str(r)+"\n")
results_file.close()
print("done.")