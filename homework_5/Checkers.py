import numpy as np

#This program does not include the commas, but still returns a checkerboard pattern
#Note: I did have a bit of help and reference from the Youtube Channel TECHNO STACK
def checkerboard():
    checkers = np.zeros((8,8),dtype=int)
    checkers[::2,::2] = 1
    checkers[1::2,1::2] = 1
    return checkers    

print(checkerboard())
