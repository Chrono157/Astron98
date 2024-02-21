def digit_root(num):
    numbers = str(num)
    sum = 0
    for i in range(len(numbers)):
        values = int(numbers[i])
        sum += values
    return sum

test = 12345
print(digit_root(test))
