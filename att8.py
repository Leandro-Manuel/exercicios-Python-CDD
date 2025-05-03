#imprima usando while

#1
#1 2
#1 2 3 ...

n = int (input('infome um número: '))

h=1
while h<=n:
    y=1
    while y<=h:
        print (y,end=" ")
        y+=1
    print()
    h+=1