def diskriminant(a, b, c):
    return b**2 - 4*a*c

a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))
D=diskriminant(a,b,c)
print("D =", D)