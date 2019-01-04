liste=[ 'coucou', 1,2,3,4,12,22,3.1416,2.0, [4,5,6]]

j=0
for i in liste:
    if type(i) is int:
            print i
        j=j+1
print j
