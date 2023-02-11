groupmates = [
    {
        "name": "Мария",
        "surname": "Шубина",
        "exams": ["Информатика", "История", "ВвИТ"],
        "marks": [4, 5, 4]
    },
    {
        "name": "Диана",
        "surname": "Крюкова",
        "exams": ["Философия", "АиГ", "Этика делового общения"],
        "marks": [5, 5, 4]
    },
    {
        "name": "Павел",
        "surname": "Никитин",
        "exams": ["Алгоритмы", "Физическая культура", "АиГ"],
        "marks": [5, 4, 5]
    },
    {
        "name": "Василий",
        "surname": "Карзанов",
        "exams": ["Русский язык", "Английский язык", "Испанский язык"],
        "marks": [5, 5, 3]
    },
    {
        "name": "Ярослав",
        "surname": "Семёнов",
        "exams": ["Физика", "ВвИТ", "Алгоритмы"],
        "marks": [3, 4, 3]
    }
]

granitsa = float(input())
groupmates = filter(lambda x: sum(x["marks"]) / len(x["marks"]) > granitsa, groupmates)

def print_students(students):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(60), u"Оценки".ljust(30))
    for student in students:
        print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(60), str(student["marks"]).ljust(30))
print_students(groupmates)



