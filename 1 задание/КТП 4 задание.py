a=[]
z=0
k=0
n=int(input("Введите количество элементов:"))
for i in range(n): 
    print("Введите ",i," элемент:")
    a.append(int(input()))
for i in  range(n):
        z=z+a[i]
        k=k+1
print("Ответ:")
print(z/k)





