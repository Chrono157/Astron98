import numpy as np

nums = np.arange(0,2*np.pi,2*np.pi/1000)
x1 = np.linspace(0,2*np.pi,1000)
x2 = 2*x1

print(x1)
print(x2)

np.mean(x1)
np.std(x1)
filtered = np.arange(101)
evens = filtered[filtered % 2 ==0]

filtered[(filtered%10==0) & (filtered%5 ==0)]