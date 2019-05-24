'use strict'

 let groupmates = [
    {
        "name" : "Гасан",
        "group" : "БСТ1703",
        "age" : 18,
        "marks" : [4, 4, 3, 5]
    },

    {
        "name" : "Марьяна",
        "group" : "БСТ1703",
        "age" : 20,
        "marks" : [2, 5, 4, 5]
    },

    {
        "name" : "Кирилл",
        "group" : "БСТ1703",
        "age" : 19,
        "marks": [3, 4, 4, 4]
    },

    {
        "name" : "Полина",
        "group" : "БСТ1702",
        "age" : 20,
        "marks" : [5, 5, 5, 5]
    },
    {
        "name" : "Александр",
        "group" : "БСТ1701",
        "age" : 20,
        "marks" : [2, 5, 4, 5]
    },
    {
        "name" : "Миша",
        "group" : "БСТ1702",
        "age" : 20,
        "marks" : [2, 5, 4, 5]
    }
]

let rpad = function(str,length){
    str=str.toString();
    while (str.length<length){
        str=str+' ';
    }
    return str;
}
let printStudents = function(students){
    console.log(
        rpad("Имя студента",15),
        rpad("Группа",8),
        rpad("Возраст",8),
        rpad("Оценки",20)
    );
    for(let i = 0; i<students.length;i++){
        console.log(
            rpad(students[i]['name'],15),
            rpad(students[i]['group'],8),
            rpad(students[i]['age'],8),
            rpad(students[i]['marks'],20),
            '\n'
        );
    }
};
printStudents(groupmates)


let filtredByGroup = function(students,groupNumber){
    for(let i =0;i<students.length;i++){
        if(groupNumber == students[i]['group']){
            console.log(
                rpad(students[i]['name'],15),
                rpad(students[i]['group'],8),
                rpad(students[i]['age'],8),
                rpad(students[i]['marks'],20),
                '\n'
            )
        }

    }
};


function makeWrap(){
    console.log("\n\n\n\n\n");
}

let filter = prompt('Введите номер группы');
makeWrap();
filtredByGroup(groupmates,filter);