def nums(a,b,c):
    if (a==b==c):
        return(3)
    elif(a==b) or (a==c) or (b==c):
        return(2)
    else:
        return(0)
n=int(input('Введите 1 число:'))
x=int(input('Введите 2 число:'))
g=int(input('Введите 3 число:'))
print(nums(n,x,g))
