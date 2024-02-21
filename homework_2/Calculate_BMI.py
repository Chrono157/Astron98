def BMI(weight,height):
    index = weight / (height**2)
    index = round(index,1)
    return index
test_weight = 68
test_height = 1.82
print(BMI(test_weight,test_height))
