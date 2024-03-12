import numpy as np

#This program utilizes the char.join function of numpy. Reference: manual
def spaceBetween(arr):
    my_newarr = np.array(arr,dtype=np.str_)
    my_newarr = np.char.join(" ",my_newarr)
    return my_newarr

myarr = np.array(['python','is','cool!'])
print(spaceBetween(myarr))