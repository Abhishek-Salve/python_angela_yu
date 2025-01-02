# Functions with outputs

# def is_leap_year(year):
#     # Write your code here.
#     # Don't change the function name.
#     if ((year % 4 == 0) or (year % 100 == 0)) and (year % 400 == 0):
#         return True
#     else:
#         return False
#
#
# print(is_leap_year(2000))
# print(is_leap_year(2400))
# print(is_leap_year(1989))
# print(is_leap_year(2100))

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


operation_dict = {}
operation_dict['+'] = add
operation_dict['-'] = subtract
operation_dict['*'] = multiply
operation_dict['/'] = divide
# print(operation_dict)
# print(operation_dict["*"](4, 8))

calculate = True
num1_old = False
operation_outcome = 0
num1 = 0

while calculate:
    if not num1_old:
        num1 = float(input("What is the first operand/number you want to use ?: "))
    else:
        print(f"Operator 1 from previous operation is : {operation_outcome}")
    operator = input ("What operator do you want to use (+ or - or * or /) ?: ")
    num2 = float(input("What is the second operand/number you want to use ?: "))

    operation_outcome = operation_dict[f'{operator}'](num1, num2)
    print(f"The result of {num1} {operator} {num2} is: {operation_outcome}")

    resume_or_new = input("Do you want to continue with the result (y/n) ?: ")
    if resume_or_new == 'y':
        num1_old = True
        num1 = operation_outcome
    else:
        num1_old = False
