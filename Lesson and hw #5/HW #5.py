# Задача #1

# Зробіть словник де буде табличка множення додавання ділення і віднімання чисел від 2 до 9(включно).
# Так як робили на уроці. Ці значення запишіть в словник з відповідними ключами "+", "-", "/", "*"
# Коли ви підготуєте це, запитайте в користувача яку табличку він хоче побачити
# (додавання, віднімання, множення, ділення). і виведіть йому цю табличку.

# =================================================================================================================


multiplication_table = {}
for i in range(2, 10):
    multiplication_table[i] = {f"{i} * {j}": i * j for j in range(2, 10)}


addition_table = {}
for i in range(2, 10):
    addition_table[i] = {f"{i} + {j}": i + j for j in range(2, 10)}


subtraction_table = {}
for i in range(2, 10):
    subtraction_table[i] = {f"{i} - {j}": i - j for j in range(2, 10)}


division_table = {}
for i in range(2, 10):
    division_table[i] = {f"{i} / {j}": i / j for j in range(2, 10)}


operation = input("Choose the operation (+, -, *, /): ")


if operation == '+':
    print(addition_table)
elif operation == '-':
    print(subtraction_table)
elif operation == '*':
    print(multiplication_table)
elif operation == '/':
    print(division_table)
else:
    print("Incorrectly selected operation.")

# ==================================================================================================================

operation_dict = {

    "+": {f"{i} + {j}": i + j for i in range(2, 10) for j in range(2, 10)},
    "-": {f"{i} - {j}": i - j for i in range(2, 10) for j in range(2, 10)},
    "*": {f"{i} * {j}": i * j for i in range(2, 10) for j in range(2, 10)},
    "/": {f"{i} / {j}": i / j for i in range(2, 10) for j in range(2, 10) if j != 0}
}

operation = input("Choose the operation (+, -, *, /): ")

if operation in operation_dict:
    print(operation_dict[operation])
else:
    print("Incorrectly selected operation.")

