import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft
import numpy as np

with open("entrada43.txt", "r") as f:
    file = f.readlines()
    
data = []
j=0
for i in range(0,len(file)):
    try:
        data.append(float(file[j]))
        j+=1
    except:
        pass
    

fft_out = fft(data)
f_delta= 1.0/365

frec =[]
L=0

for i in data:
    frec.append(L*f_delta)
    L+=1
    
filtered = []
L=0

for i in data:
    if L < 15 and L>5:
        filtered.append(fft_out[L])
    else:
        filtered.append(0)
    L+=1
    
time =[]
time.extend(range(0,len(data)))
inverse = np.abs(ifft(filtered))
plt.plot(time, data)
plt.plot(time, inverse)
plt.show()
    