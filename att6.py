# imprima usando while

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

num = int (input('Digite um número: '))

n = 1

while n <= num:
    print (n*str(n),end=" ")
    n+=1