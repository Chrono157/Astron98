def rotate_digits(n):
    num = n // 10
    first_num = n % 10
    count = 0
    if n % 10 != 0:
        new_num = num
        while new_num % 10 != 0:
            count += 1
            new_num = new_num // 10
    else:
        first_num = 0
    first_num = first_num * (10**count)
    result = first_num + num
    return result

test = 12340
print(rotate_digits(test))
#This program works as intended, except when the last digit is a 0. It cannot display the 0 at the end at the beginning and instead just truncates it instead which works numerically because 0's at the beginning are usually invisible...
 