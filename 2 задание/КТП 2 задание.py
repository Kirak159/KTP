l=[]
print("Введите количество элементов")
z=int(input())
for i in range(z):
    print("Введите ",i," элемент")
    l.append(input())
for i in range(z):
    le=l[i]
    if(le[len(l[i])-1]=='r'):
        print(l[i])



