def leap_year_check(year):
    leap_year = False
    if year % 4 == 0:
        leap_year = True
    if year % 100 ==0:
        leap_year = False
    if year % 400 ==0:
        leap_year = True
    return leap_year

test = 1900
print(leap_year_check(test))