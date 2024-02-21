def for_maximum(num_list):
    maximum = num_list[0]
    for i in range(len(num_list)):
        if num_list[i] > maximum:
            maximum = num_list[i]
    return maximum

def while_maximum(num_list):
    maximum = num_list[0]
    i = 1
    while i < len(num_list):
        if num_list[i] > maximum:
            maximum = num_list[i]
        i+=1
    return maximum

def for_minimum(num_list):
    minimum = num_list[0]
    for i in range(len(num_list)):
        if num_list[i] < minimum:
            minimum = num_list[i]
    return minimum

def while_minimum(num_list):
    minimum = num_list[0]
    i = 1
    while i < len(num_list):
        if num_list[i] < minimum:
            minimum = num_list[i]
        i+=1
    return minimum

test = [18,38,24,31,48]
print(for_maximum(test))
print(while_maximum(test))
print(for_minimum(test))
print(while_minimum(test))