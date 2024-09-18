# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

exec_homeworks_count = 12
time_stemp = 1.5
course_name = 'python'
time_per_one_homework = time_stemp / exec_homeworks_count

# рекомендованный способ (почему-то включаются лишние пробелы)
print('Курс:',course_name,',всего задач:',exec_homeworks_count,',затрвчено часов:',time_stemp,',среднее время выполнения:',time_per_one_homework)

#  печать с форматированием (дает заданный результат)
print(f'Курс: {course_name}, всего задач:{exec_homeworks_count}, затрвчено часов:{time_stemp}, среднее время выполнения:{time_per_one_homework}')