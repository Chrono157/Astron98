import numpy as np

"""This program is slightly convuluted, but it does the trick.
#Instead of returning an array that has no gaps, it returns an array with gaps to show the lines that do not have all the same numbers
This is entirely unintentional, but it works decently, so I'm not complaining. I also could not find any commands that simplifies this
so I just did it manually"""
def findEqual(array):
    myArr = np.array([])
    my_newlist = []
    for i in range(array.shape[0]):
        for j in range(array.shape[1]-1):
            if array[i][j] != array[i][j+1]:
                break
            if j == array.shape[1]-2:
                my_newlist.append([np.append(myArr,array[i,:],axis=0)])
    my_newarr = np.array(my_newlist,dtype=int)
    return my_newarr

arr = np.array([[1,1,1],[1,2,3],[2,2,2]])
print(findEqual(arr))


