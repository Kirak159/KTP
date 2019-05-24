a=[]
n=int(input("Введите количество элементов:"))
for i in range(n): 
    print("Введите ",i," элемент:")
    a.append(str(input()))
for i in  range(n):
    if(i%2==0):
        print(a[i])





