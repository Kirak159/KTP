#coding:utf-8

groupmates = [
    {
        "name" : u"Гасан",
        "group" : u"БСТ1703",
        "age" : 18,
        "marks" : [4, 4, 3, 5]
    },

    {
        "name" : u"Марьяна",
        "group" : u"БСТ1703",
        "age" : 20,
        "marks" : [2, 5, 4, 5]
    },

    {
        "name" : u"Кирилл",
        "group" : u"БСТ1703",
        "age" : 19,
        "marks": [3, 4, 4, 4]
    },

    {
        "name" : u"Полина",
        "group" : u"БСТ1703",
        "age" : 20,
        "marks" : [5, 5, 5, 5]
    }
]

ave_rate = float(input("Введите среднюю оценку:  "))
print("\n")

def print_students(students):
    print( u"Имя студента".ljust(15), \
          u"Группа".ljust(8), \
          u"Возраст".ljust(8), \
          u"Оценки".ljust(20) )
    for student in students:
        print( student["name"].ljust(15), \
              student["group"].ljust(8), \
              str(student["age"]).ljust(8), \
              str(student["marks"]).ljust(20) )
        print("\n")

def average_rating(students, ave_rate):
    ave = []
    for student in students:
        if(float(sum(student["marks"]) / len(student["marks"])) >= ave_rate):
            ave.append(student["name"])

    for student in students:
        if(student["name"] in ave):
            print( student["name"].ljust(15), \
                student["group"].ljust(8), \
                str(student["age"]).ljust(8), \
                str(student["marks"]).ljust(20) )
            print("\n")


average_rating(groupmates, ave_rate)