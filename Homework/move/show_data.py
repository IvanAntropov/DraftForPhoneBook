
from view import simple_print as sp
from view import input_values_for_digits as inputD

from data import read_all_numbers as rA
from data import read_numbers_in_file as rS

def all_numbers():
    string = rA()
    for i in range(len(string)):
        sp(string[i])

# def specific_file():
#     sp(rS)

def show_numbers():
    all_numbers()

    # choice = inputD('\n1)Все номера\n2)Из конкретного файла','Error. Try again',1,2)
    # match choice:
    #     case 1:
    #         all_numbers()
    #     case 2:
    #         specific_file()