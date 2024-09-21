
# Список оценок, упорядоченный по именам студентов
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]

# Неупорядочное множество имен студентов
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Преобразуем множество в список
students_list = list(students)

# Упорядочим список
students_list.sort()

# Создаем словарь успеваемости в нужном формате и делаем его пустым
grade_dictionary = {'name': 0.0}
grade_dictionary.pop('name')

# Наполняем словарь
students_index = 0
for current_student in students_list:

    # Вычисляем среднюю оценку
    ave_grade = 0.0
    for current_grade in range(0,len(grades[students_index])):
        ave_grade += grades[students_index][current_grade] / len(grades[students_index])

    # Заносим в словарь имя студента и среднюю оценку
    grade_dictionary[current_student] = ave_grade
    students_index += 1

print(grade_dictionary)