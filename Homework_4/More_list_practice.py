"""I had many run-type errors caused by logic mistakes. Most of them were due to the fact that count2 was not updating correctly
and oftentimes ended up as a negative number. This was because I tried to dynamically update count2 everytime I removed a variable. 
This method works for count because the loop would automatically add the subtracted value at the end of the loop, causing no issue,
but with count 2, it only increases at the end of the inner loop, which caused it to be much less than I wanted.
Originally I used 2 for loops, but realized this was a bad idea because the amount of repitition of a for loop can't be changed after
it has been declared. To fix this, I just used a while loop instead with a dynamically updating bound rather than value.

Along the way, I ran into several IndexErrors that I fixed by redoing the logic and bounds of my loops or how my variables dynamically
updated. The latest IndexError was because I had <= as the condition for count_max, which would have given me a value 1 greater than the max.
Admittedly this code is a bit complex, but it works fine. Now that I think about it, I could have probably used 2 while loops instead of
dynamically changing my counter variables and instead just dynamically changing the condition for the loop, but it's too late."""
def removeDuplicates(num_list):
    count2 = 0
    count_max = len(num_list)
    while count2 < count_max:
        count = 0
        for j in range(len(num_list)):
            if count2 != count:
                if num_list[count2] == num_list[count]:
                    num_list.remove(num_list[count])
                    count -= 1
                    count_max-=1
            count += 1
        count2 += 1
    return num_list

lis = [1,1,1,2,2,3,3,4,4,5]
print(removeDuplicates(lis))        