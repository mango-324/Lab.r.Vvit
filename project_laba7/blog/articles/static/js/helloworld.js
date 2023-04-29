var groupmates = [
    {
        "name": "Мария",
        "surname": "Шубина",
        "group": "БФИ2202",
        "marks": [5, 5, 5, 5, 5]
    },
    {
        "name": "Иван",
        "surname": "Иванов",
        "group": "БФИ2202",
        "marks": [4, 4, 4, 4, 4]
    },
    {
        "name": "Василий",
        "surname": "Васильев",
        "group": "БФИ2202",
        "marks": [3, 3, 3, 3, 3]
    },
    {
        "name": "Михаил",
        "surname": "Михайлов",
        "group": "БСТ2201",
        "marks": [5, 5, 5, 5, 5]
    },
    {
        "name": "Александр",
        "surname": "Александров",
        "group": "БВТ2201",
        "marks": [4, 4, 4, 4, 4]
    },
];

var rpad = function(line, length) {
    line = line.toString(); // преобразование в строку
    while (line.length < length)
        line = line + ' '; // добавление пробела в конец строки return str; // когда все пробелы добавлены, возвратить строку
    return line;
};

var printStudents = function(students){ 
    console.log(
        rpad("Имя", 15),
        rpad("Фамилия", 15),
        rpad("Группа", 8),
        rpad("Оценки", 20)
    );
    // был выведен заголовок таблицы
    for (var i = 0; i <= students.length-1; i++){
        console.log(
            rpad(students[i]['name'], 15),
            rpad(students[i]['surname'], 15),
            rpad(students[i]['group'], 8),
            rpad(students[i]['marks'], 20)
        );
    }
    console.log('\n'); // добавляется пустая строка в конце вывода
};

var filterGroup = function(students, group) {
    var mass = []
    for (var i = 0; i < students.length; i++) {
        if (students[i]['group'] == group) {
            mass.push(students[i]);
        }
    }
    return mass;
}

var filterMark = function(students, mark) {
    var mass = []
    for (var i = 0; i < students.length; i++) {
        summ = students[i]['marks'].reduce((a, b) => a + b, 0);
        if (summ / students[i]['marks'].length > mark) {
            mass.push(students[i])
        }
    }
    return mass;
}

var fl_group = prompt("Введите группу для фильтрации:")
printStudents(filterGroup(groupmates, fl_group));
var sr_mark = prompt("Введите среднюю оценку:");
printStudents(filterMark(groupmates, sr_mark));	



