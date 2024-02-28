##part 1
##I had an IndexError and am attempting to correct it by using the append function now it works fine
num_list = []
for i in range(0,50):
    num_list.append(i+1)
print (num_list)
copy_num_list = num_list
print(copy_num_list)

##part 2
def square(nums):
    temp_list = nums
    for i in range(len(nums)):
        temp_list[i] = nums[i] * nums[i]
    return temp_list

lis = [2,3,4]
print(square(lis))

##part 3
"""Had a type error because I mistakingly used the range function instead of just the list name
Ran into another TypeError because num is a list and not a number, so I'm using the int function
It didn't work and I'm a bit confused with how for loops work so I'll resort to using a counter, which is what I'm more used to
It worked perfectly with an index.
Actually, switching the numbers revealed that the function actually didn't work. Still had an index error
I realized this was because the counter variable i was not taking into account the fact that remove shortens the list by 1
To fix this, I defined another counter variable named count that would dynamically adjust and now it works fine"""
def sorted_combination(listA, listB):
    temp_list = listA + listB
    count = 0
    for i in range(len(temp_list)):
        if temp_list[count] % 2 == 0:
            temp_list.remove(temp_list[count])
            count-=1
        count += 1
    temp_list.sort()
    return temp_list

list1 = []
for i in range(9,0,-1):
    list1.append(i)

list2 = []
for j in range(29,20,-1):
    list2.append(j)
print(sorted_combination(list1,list2))

