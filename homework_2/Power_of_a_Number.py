def pow(num,power):
    product=num
    for i in range(power-1):
        product*=num
    return product

test = 3
exponent = 5
print(pow(test,exponent))
