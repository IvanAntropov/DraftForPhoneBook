# path_to_file = 'Phone_books/phone_book.word'
# numbers = [("ivan antropov", 79630444553),("alex antropov", 79630444554),("anna antropova", 79090105475)]
# # names = ["ivan antropov", "alex antropov", "anna antropova"]
# # numbers = [79630444553, 79630444553, 79630444553]
# # string = list(zip(numbers,names))
# string = ''
# for i in range(len(numbers)):
#     string+= str(numbers[i][0]) + ' ; ' + str(numbers[i][1]) + ';\n'
# print(string)
# with open (path_to_file, 'a') as fr:
#     fr.write(string)

# with open (path_to_file, 'r') as fr:
#     numbers = fr.read()

# print(numbers)

# def wind_speed_logger(data):
#     time = dt.now().strftime('%H:%M')
#     with open('ex2\log.csv', 'a') as file:
#         file.write('{};wind_speed;{}\n'
#                     .format(time, data))
# from view import simple_print as sp
# from view import input_values_for_digits as inputD
# from view import input_values_for_strings_with_check as inputSC
# from view import input_values_for_strings_for_names as inputN
# from view import input_values_for_escape as esc

# listInput = []
# name = inputN('Введите имя: ')
# phone_number = inputD('Введите телефон без "+":','Error. Try again',7900000000,8999999999)
# listInput.append(name)
# listInput.append(phone_number)
# print(listInput)