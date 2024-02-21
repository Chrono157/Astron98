def vowels(words):
    count = 0
    for i in range(len(words)):
        if words[i] == "A" or words[i] == "a" or words[i] == "E" or words[i] == "e" or words[i] == "I" or words[i] == "i" or words[i] == "U" or words[i] == "u":
            #very long conditional, but it works. I could have separated this into multiple lines, but I didn't want to
            count +=1
            print(words[i])
    return count

test = "UC Berkeley"
print(vowels(test))
