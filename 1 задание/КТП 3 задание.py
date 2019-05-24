a=[]
z=1
n=int(input("Введите количество элементов:"))
for i in range(n): 
    print("Введите ",i," элемент:")
    a.append(int(input()))
for i in  range(n):
    if(a[i]<10):
        z=z*a[i]
print("Ответ:")
print(z)





