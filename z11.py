
#str = input('Ввидите строку : ')
#str2 = str.split()
#print(len(str2))


a = [5,[1,2],2,'r',4,'ee']
b = [4,'we','ee',3,[1,2]]
d = []
for i in a:
    if i in b:
        d.append(i)
print(d)


