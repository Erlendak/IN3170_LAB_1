import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


DATA_FOLDER = "../lab1_data/task1/"
NFET_FILES = ["ngate1.5v.txt","ngate2v.txt", "ngate3v.txt", 
              "ngate5v.txt", "ngate10v.txt"]
PFET_FILES = ["pgate1.5v.txt","pgate2v.txt", "pgate3v.txt",
             "pgate5v.txt", "pgate10v.txt"]

COLORS = ["r","g","b","y","m"]
INC = 0.25

def line(x1, x2, y1, y2):    # Two-point formula for a straight line 
    return lambda x: (y2-y1)*(x-x1)/(x2-x1) + y1      




###### N-channel MOSFET transistor ######

sat_i = int(6/INC) # Index for definite saturation of nfets. v_GS=6V-ish

for j, nfet in enumerate(NFET_FILES):
    data = pd.read_table(
        DATA_FOLDER+nfet, 
        decimal=',', 
        skiprows=2).values
    v = data[:-4,0];    i = data[:-4,1]

    iv_label = r"$v_{GS}=$"+nfet.replace("ngate","").replace(".txt","")
    plt.plot(v, i, COLORS[j], label=iv_label)

    v_early = np.linspace(-300, v[sat_i], 300)
    early_line = line(v[sat_i],v[-8],i[sat_i],i[-8])   # v[-8] is experimentally tested to work fine for early voltage line
    plt.plot(v_early, early_line(v_early), COLORS[j]+"--", label='_nolegend_' ) 

plt.grid()
plt.legend()
plt.ylabel(r"Current $i_{DS}$", size=15)
plt.xlabel(r"Voltage $v_{DS}$", size=15)
plt.title(r"$i_{DS}$ vs. $v_{DS}$ Plot Characteristics", size=17)
plt.savefig("nmos_early.png")
plt.show()




###### P-channel MOSFET transistor ######

sat_i = int(7.5/INC) # Index for definite saturation of pfets. v_GS=-7.5V-ish

for j, pfet in enumerate(PFET_FILES):
    data = pd.read_table(
        DATA_FOLDER+pfet, 
        decimal=',', 
        skiprows=2).values
    v = data[:-4,0][::-1];    i = data[:-4,1][::-1]
    iv_label = r"$v_{GS}=$"+pfet.replace("pgate","").replace(".txt","")
    plt.plot(v, i, COLORS[j], label=iv_label)

    v_early = np.linspace(v[sat_i], 40, 40)
    early_line = line(v[-2],v[sat_i], i[-2],i[sat_i])
    plt.plot(v_early, early_line(v_early), COLORS[j]+"--", label='_nolegend_' ) 

plt.grid()
plt.legend()
plt.ylabel(r"Current $i_{DS}$", size=15)
plt.xlabel(r"Voltage $v_{DS}$", size=15)
plt.title(r"$i_{DS}$ vs. $v_{DS}$ Plot Characteristics", size=17)
plt.gca().invert_xaxis()
plt.gca().invert_yaxis()
plt.savefig("pmos_early.png")
plt.show()
