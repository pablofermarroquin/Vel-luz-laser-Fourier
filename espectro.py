import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft
import numpy as np
from scipy.interpolate import make_interp_spline
import matplotlib.patches as mpatches

with open("espectro-salida-ejeX.txt", "r") as f:
    file1 = f.readlines()
    
with open("espectro-salida-ejeY.txt", "r") as f:
    file2 = f.readlines()
    
#with open("tiempo.txt", "r") as f:
#    file3 = f.readlines()
    
data1 = []
data2 = []
time =[]
for i in range(0,len(file1)):
    #try:
    data1.append(float(file1[i]))
    data2.append(float(file2[i]))
    #time.append(float(file3[i]))
    #except:
     #   pass
    
X_Y_Spline = make_interp_spline(data1, data2)
X = np.linspace(np.array(data1).min(), np.array(data1).max(), 500)
Y = X_Y_Spline(X)

id_xc= mpatches.Patch(color='green', label='d = 0.43 m')
id_xp= mpatches.Patch(color='blue', label='d = 0.73 m')
id_xTOT= mpatches.Patch(color='red', label='d = 1.29 m')
plt.legend(handles=[id_xc, id_xp,id_xTOT])

plt.xlabel("Frecuencia (Hz)")
#plt.ylabel("Posición (m)")
plt.title("Espectro de frecuencias") 


plt.plot(X, Y, c="green")
plt.plot(X, Y+3, c="blue")
plt.plot(X, Y+6, c="red")
plt.show()
    