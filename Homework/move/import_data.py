
from view import simple_print as sp
from view import input_values_for_digits as inputD
from view import input_values_for_strings_with_check as inputSC
from view import input_values_for_strings_for_names as inputN
from view import input_values_for_escape as esc

from data import append_numbers as a

def manual_input():
    check = False
    mainList = []
    while not check:
        listInput = []
        name = inputN('Введите имя: ')
        phone_number = inputD('Введите телефон без "+":','Error. Try again',79000000000,89999999999)
        listInput.append(name)
        listInput.append(phone_number)
        mainList.append(listInput)
        check = esc()
    return mainList

# def numbers_from_file():
#     path_to_file = inputN('Введите путь к файлу: ')
#     mainList = []
#     with open (path_to_file, 'r') as fr:
#         for i in range(len(fr.readline.split(';'))/2):
#             numbers = []
#             numbers = fr.readline.split(';')
#             mainList.append(numbers)
#     return mainList

def start_import():
    a(manual_input())

    # choice = inputD('Как?\n1)Вручную\n2)Из другого файла\nВвод: ','Error. Try again',1,2)
    # match int(choice):
    #     case 1:
    #         a(manual_input())
    #     case 2:
    #         a(numbers_from_file())