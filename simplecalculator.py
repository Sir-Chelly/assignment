# Name: Idima Ikenna Uzochi
# Reg: 2017364004
# Dept: ECE 
# Course: ECE 541
# Lecturer: Engr Dozie

print('Select Operation to perform.' 'Eg: 1 to ADD, 2 to SUBSTRACT, 3 to MULTIPLY, 4 to DIVIDE')
# print('1. ADD')
# print('2. SUBSTRACT')
# print('3. MULTIPLY')
# print('4. DIVIDE')

operation = input()

if operation == '1':
    #code for add
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
    print('The result of ' + str(num1) + ' + ' + str(num2)+ ' = ' + str(num1 + num2))

elif operation == '2':
    #code for substract
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
    print('The result of ' + str(num1) + ' - ' + str(num2)+ ' = ' + str(num1 - num2))

elif operation == '3':
    #code for multiply
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
    print('The result of ' + str(num1) + ' * ' + str(num2)+ ' = ' + str(num1 * num2))

elif operation == '4':
    #code for division
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
    print('The result of ' + str(num1) + ' / ' + str(num2)+ ' = ' + str(num1 / num2))

else:
    print('Invalid entry')
