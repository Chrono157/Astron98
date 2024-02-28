##part 1
list = []
for i in range(5):
    listadd = []
    for j in range(5):
        listadd.append((i*5)+(j+1))
    list.append(listadd)

"""this results in the expected output but without the extra square bracket
This also uses a for loop to print out the list because just outrighting printing the list creates the list on 1 line"""
for count in range(5):
    print(list[count])

print() ##just to put a space between the two arrays

##part 2
list = []
for i in range(5):
    listadd = []
    for j in range(5):
        listadd.append((i*5)+(j+1))
        if listadd[j] % 3 == 0:
            listadd[j] = "?"
    list.append(listadd)

"""this results in the expected output but without the extra square bracket
This also uses a for loop to print out the list because just outrighting printing the list creates the list on 1 line"""
for count in range(5):
    print(list[count])