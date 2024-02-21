def min_and_max(num_list):
    maximum = num_list[0]
    minimum = num_list[0]
    for i in range(len(num_list)):
        if num_list[i] > maximum:
            maximum = num_list[i]
        if num_list[i] < minimum:
            minimum = num_list[i]
    results = ("maximum:", maximum, "minimum:", minimum)
    return results

test = [46,8,25,14,50]
print(min_and_max(test))
