import matplotlib.pyplot as plt

file = open("task2_nmos.txt", "r")
file.readline()

def convert(str):
    strs = str.split(',')
    strcombine = strs[0] + '.' + strs[1]
    return float(strcombine)

voltage = []
current = []

for line in file:
    words = line.split()
    voltage.append(words[0])
    current.append(words[-1])

for i in range(len(voltage)):
    voltage[i] = convert(voltage[i])

for i in range(len(current)):
    current[i] = convert(current[i])


plt.plot(voltage, current)
plt.xlabel("vDS")
plt.ylabel("iDS")
#plt.yscale('log')
#plt.title("iDS vs vDS for n_gate with 10v")
#plt.xticks([])
#plt.yticks([])
plt.show()
