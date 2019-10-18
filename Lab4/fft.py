#############FFT######################
import numpy as np
import math
from matplotlib import pyplot as plt
N=64 # es el tamano del vector. Tambien se toma como el orden de la FFT
k=1
fo=3000
n=np.linspace(0,N-1,N)
Fsamp=80000
signal=np.exp(1.j*2.*math.pi*fo*n/Fsamp)
fourier=np.fft.fft(signal)

fourier_mejor=np.fft.fftshift(fourier)

fourier_magnitude=np.square(abs(fourier_mejor))
# calculos para poder adornar la grafica con valores del mundo real
T=1./fo
Ts=T/N
Fs=1./Ts
Fmin=-Fs/2.
Fresol=Fs/N
Fmax=-Fmin-Fresol
f=np.linspace(Fmin,Fmax,N)
plt.plot(f,fourier_magnitude)
plt.show()