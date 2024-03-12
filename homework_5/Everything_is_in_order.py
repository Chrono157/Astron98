import numpy as np

#This is also a very simple program using the sort command. I referenced the numpy manual, specifically the one with sort
#This program takes an array of random numbers and sorts the columns from least to greatest 
def sorting(arr):
    my_newarr = np.sort(arr,axis=0)
    return my_newarr

np.random.seed(12345)
a = np.random.random_integers(1,50, (4,5))
print(a)
print() #just to put a gap between the original and the sorted
print(sorting(a))