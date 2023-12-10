# Задача 1

# Напишіть програму яка запитує в користувача вартість покупок, він їх вводе через пробіл, точна кількість не вказана.
# Вам потрібно до вартості покупок додати 6,5 відсотки податків.
# Потім питаєте чи є в користувача купон на знижку якщо є то питаєте це на суму чи на відсоток і потім віднімаєте суму
# або відсоток відповідно від ціни яку отримали раніше і пишете користувачу кінцеву суму.


entering_the_purchase_price = input("Enter purchase quantity: ")

purchase_prices = entering_the_purchase_price.split()

total_price = sum(float(price) for price in purchase_prices)

price_with_tax = total_price * 1.065

print(f"Total cost of purchases with tax: {price_with_tax:.2f}")

discount_coupon = input("Do you have a discount coupon? (yes/no): ").lower()

if discount_coupon == 'yes':
    discount_type = input("It is a discount on the amount or percentage? (amount/percent): ").lower()
    if discount_type == 'amount':
        discount_amount = float(input("Enter the discount amount: "))
        final_price = price_with_tax - discount_amount
    elif discount_type == 'percent':
        discount_percent = float(input("Enter the discount percentage: "))
        final_price = price_with_tax * (1 - discount_percent / 100)
    else:
        print("Invalid discount type.")
        final_price = price_with_tax
else:
    final_price = price_with_tax

print(f"The final amount after applying the discount: {final_price:.2f}")

# ====================================================================================================================

# Задача 2

# Переробіть задачу з попереднього уроку враховуючи ваші знання з цього уроку, використайте цикл for in або while.

shopping_cart = []
for _ in range(5):
    item = input("Enter an item: ")
    shopping_cart.append(item)

print("Your current shopping cart:")
print(shopping_cart)

while len(shopping_cart) > 0:
    remove_choice = input("Do you want to remove an item from the cart? (yes/no): ").lower()

    if remove_choice == 'yes':
        removed_item = shopping_cart.pop(0)
        print(f"Removed {removed_item} from the cart.")
        print("Updated shopping cart:", shopping_cart)
    else:
        break

if not shopping_cart:
    print("Your shopping cart is empty.")
else:
    print("Final Shopping Cart:", shopping_cart)


# ====================================================================================================================

# Задача 3

# Напишіть програму Банкомат. Втсановіть пін код для користувача(зробимо це константою).
# Запитайте в користувача Пін якщо він введе три рази не вірно то напишіть що карта заблокована.
# Використовуйте цикл while.


PIN_CODE = "5555"

attempts = 3

while attempts > 0:
    entered_pin = input("Enter your PIN code: ")

    if entered_pin == PIN_CODE:
        print("Entry allowed. Welcome !")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Incorrect PIN code. Attempts left: {attempts}")
        else:
            print("The card is blocked. Contact your personal manager.")

# ====================================================================================================================

# Задача 4

# Напишіть за допомогою f-string та format. Дві стрічки де буде підставлятись імя та вік з зміних
# name = "оЛенА"
# age = 21
# f_string = тут ваш код формата ф-стрінг. | повино вийти -> Я Олена, мені 21 рік
# format_string = тут ваш код формата формат стрінг | повино вийти -> Я Олена, мені 21 рік
# print(f_string)
# print(format_string)

name = "оЛеНа"
age = 21

f_string = f"Я {name.capitalize()}, мені {age} рік"

format_string = "Я {}, мені {} рік".format(name.capitalize(), age)

print(f_string)
print(format_string)
