mylist = list(range(1, 10, 2))
mylist2 = list(range(0, 10, 2))

mylist.extend(mylist2)

mylist = [2 * i for i in mylist]

for i in mylist:
    print(type(i))