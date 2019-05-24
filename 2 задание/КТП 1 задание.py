
import random
my_number=random.randint(1,10)
print(my_number)
print("Введите число user_number")
user_number=float(input())

while(user_number==my_number):
    print("Введите число user_number")
    user_number=float(input())


