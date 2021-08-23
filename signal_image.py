#creates signal and then creates the digital fourier transform (DFT) of that signal
import matplotlib.pyplot as plt
import numpy as np

#sampling rate
sr = 128
#interval
Ts = 1/sr
#range
t = np.arange(0,1,Ts)

def s(n):
    f = 1
    x = 4*np.sin(2*np.pi*f*n)
    f = 10
    x += 2*np.sin(2*np.pi*f*n)
    f = 20
    x += 10*np.sin(2*np.pi*f*n)
    return x


def DFT(s):
    N = len(s)
    n = np.arange(N)
    k = n.reshape((N, 1))
    re = np.cos(2*np.pi*k*n/N)
    im = np.sin(2*np.pi*k*n/N)
    Xr = np.dot(s, re)
    Xi = np.dot(s, im)
    Xp = (Xr**2) + (Xi**2)
    return Xp

X = DFT(s(t))

N = len(X)
n = np.arange(N)
T = N/sr
freq = n/T 

fig, axs = plt.subplots(2)    
axs[0].plot(t, s(t))
axs[0].set_title("Signal")
axs[1].stem(freq, X)
axs[1].set_title("DFT")
plt.show()
