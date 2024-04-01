import os

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mult(num1,num2):
    return num1 * num2

def div(num1,num2):
    return num1 / num2

possible_Result = ['No','nO','NO','no']

propertys = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div
}

# Main
loop = True

num1 = float(input("Write a number: "))
for symbol in propertys:
    print(symbol)
operation = input("Choose one action: ")
num2 = float(input("Write the second number: "))
choosen_operation = propertys[operation]
result = choosen_operation(num1,num2)
print(f'{num1} {operation} {num2} = {result}')

continue_operation = input("Want to continue [yes/no]: ")
if continue_operation in possible_Result: 
    print("Thank you for using the calculator!!")
    loop = False
else: 
    while loop:
        os.system("cls")
        previous_result = result
        print(f"The previous result is: {previous_result}")
        for symbol in propertys:
            print(symbol)
        operation = input("Choose one action: ")
        num2 = float(input("Write the second number: "))
        choosen_operation = propertys[operation]
        result = choosen_operation(previous_result,num2)
        print(f'{previous_result} {operation} {num2} = {result}')

        continue_operation = input("Want to continue [yes/no]: ")
        if continue_operation in possible_Result: 
            print("Thank you for using the calculator!!")
            loop = False

