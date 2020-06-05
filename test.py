import itertools as it
liste =[1,2,3,4,5,6,7]
big_list =[]
it.combinations(liste, 1)
for i in range(1,len(liste)+1):
    liste = list(it.combinations(liste, i))

    big_list.append(liste)
    for c in liste:
        print(c)

