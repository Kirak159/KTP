
print("Введите число а")
a=float(input())
print("Введите число b")
b=float(input())
print("Введите число c")
c=float(input())
if c-a == 0 :
    print("Деление на ноль")
else:
    z=abs(1-a*pow(b,c)-a*(b*b-c*c)+(b-c+a)*(12+b)/(c-a))
    print("Ответ:")
    print(z)
