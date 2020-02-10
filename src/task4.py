import matplotlib.pyplot as plt
import numpy as np


FILENAME = "../lab1_data/task4/oppgave4_IO.txt"



inputs  = []
outputs = []

with open(FILENAME, "r") as infile:
    for i in range(5):
        infile.readline()

    for line in infile:
        data_list = line.split()
        inputs.append(  float(data_list[2].replace(",","."))  )
        outputs.append(  float(data_list[5].replace(",","."))  )


plt.grid()
plt.plot(inputs[190:-750])
plt.plot(outputs[190:-750])
plt.legend(["Input voltage","Output voltage"])
plt.ylabel("Voltage (V)", size=15)
plt.xlabel("Timesteps", size=15)
plt.title("Input-Output relationship of an inverter", size=16)
plt.savefig("io_inverter.png")
plt.show()