#This is an example of how to use lists in practice
planets = []
planets.append("Mercury")
planets.append("Earth")
planets.append("Mars")
print(planets)

planets.insert(1,"Venus")
print(planets)
print(planets[2])

planets[3]="Ares"
print(planets)

planets.append("Jupiter")
print(planets)
planets.remove("Jupiter")
print(planets)

print(len(planets))

#This is an example of how to use dictionaries
fourth_planet = {"name": "Mars", "moons":["Phobos", "Deimos"], "atmosphere": False}
print(fourth_planet)
fourth_planet["atmosphere"]=True
print(fourth_planet)

nums = [1,2,3,4,5,6,7,8,9]
sliced = nums[1:9]
print(len(sliced))
print(sliced)
reversed = nums[8::2]
print(reversed)
reversed1 = nums [8::-2]
print(reversed1)

list_1 = ["a","b","c"]
list_2 = [17,18,19]
add = list_1+list_2
print(add)
list_3 = [True,False,False]
list_1.extend(list_3)
print(list_1)
add.extend(list_3) #extend does elements while append just takes the things
print(add)
desserts = ["cookie", "icecream", "brownie", "candy"]
c_words = [dessert.upper() for dessert in desserts if dessert.startswith('c')]
print(c_words)

friends_fav_nums = {"Alice": [5,101,66], "Bob": [7,23,111], "Chuck":[26,82,84]}
average_nums = {name : sum(num)/len(num) for name, num in friends_fav_nums.items()}
print(average_nums)