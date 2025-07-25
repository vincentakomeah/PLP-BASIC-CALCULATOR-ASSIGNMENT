# This prints 'PLP BASIC CALCULATOR ASSIGNMENT'
print('PLP BASIC CALCULATOR ASSIGNMENT\n')
# This allows for the first number input.
first_num = input("Enter first number: \n")
# This allows for the symbol input.
symbols = input("Enter '+,-,*,/': \n")
# This allows for the second number input.
second_num = input("Enter the second number: \n")

# This conditions checks the addition operation and prints the answer.
if symbols == '+':
    equal = int(first_num) + int(second_num)
    print(f"\nThe answer is: {equal}")
# This conditions checks the subtraction operation and prints the answer.
elif symbols == '-':
    equal = int(first_num) - int(second_num)
    print(f"\nThe answer is: {equal}")
# This conditions checks the multiplication operation and prints the answer.
elif symbols == '*':
    equal = int(first_num) * int(second_num)
    print(f"\nThe answer is: {equal}")
# This conditions checks the division operation and prints the answer.
elif symbols == '/':
    equal = float(first_num) / float(second_num)
    print(f"\nThe answer is: {equal}")

