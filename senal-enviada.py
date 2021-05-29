import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft
import numpy as np
from scipy.interpolate import make_interp_spline
import matplotlib.patches as mpatches

with open("tiempo.txt", "r") as f:
    fileT = f.readlines()

with open("salida43.txt", "r") as f:
    file1 = f.readlines()
    
with open("salida73.txt", "r") as f:
    file2 = f.readlines()
    
with open("salida129.txt", "r") as f:
    file3 = f.readlines()
    
T=[]
data1 = []
data2 = []
data3 =[]
for i in range(0,len(file1)):
    #try:
    T.append(float(fileT[i]))
    data1.append(float(file1[i]))
    data2.append(float(file2[i]))
    data3.append(float(file3[i]))
    #except:
     #   pass

id_xc= mpatches.Patch(color='green', label='d = 0.43 m')
id_xp= mpatches.Patch(color='blue', label='d = 0.73 m')
id_xTOT= mpatches.Patch(color='red', label='d = 1.29 m')
plt.legend(handles=[id_xc, id_xp,id_xTOT])

plt.xlabel("Tiempo (s)")
#plt.ylabel("Posición (m)")
plt.title("Señal de salida") 


plt.plot(T, data1, c="green")
plt.plot(T, data2, c="blue")
plt.plot(T, data3, c="red")
plt.show()
    