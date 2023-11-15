# Задача 1

# Уявимо що до нас прийшов наш друг або подруга і попросили написати додаток для покупок в магазині
# що б можна було скласти список продуктів та коли купуєш викреслювати(для викреслення питайте номер елемента,
# що б видалити по індексу треба його передати в pop list_a.pop(0) - видалить нульовий індекс, памятайте що користувач
# не знає що в нас індекси починаються з нуля). Також нам відомо що цей список має пять або більше елементів.
# Після кожного видалення елементу виводьте наш оновлений список.
# Після 5 видалень перевірте чи список пустий якщо не пустий напишіть що ось ще є продукти, якщо пусти то напишіть про це.
# Також після цього кроку запропонуйте користувачу написати ще продуктів та додати його в кошик.
# і виведіть їх на екран. Але цього разу вже без видалень.

# Кроки:

# Спочатку пропонуємо користувачу ввести продукти.
# Робимо 5 запитів на видалення
# Перевіряємо корзину
# Пропонуємо додати продукти
# Виводмо список і прощаємось

# ====================================================================================================================

# Рішення:

txt_to_display_initial = "Shopping Cart: "
txt_to_display_when_delete = "Write product number to delete: "

list_a = input(txt_to_display_initial)
list_a = list_a.replace(', ', ',').split(",")

if len(list_a):
    prod_num_to_delete = int(input(txt_to_display_when_delete)) - 1
    if prod_num_to_delete <= len(list_a) - 1 and prod_num_to_delete >= 0:
        list_a.pop(prod_num_to_delete)
    print(f'Products list: {list_a}')

if len(list_a):
    prod_num_to_delete = int(input(txt_to_display_when_delete)) - 1
    if prod_num_to_delete <= len(list_a) - 1 and prod_num_to_delete >= 0:
        list_a.pop(prod_num_to_delete)
    print(f'Products list: {list_a}')

if len(list_a):
    prod_num_to_delete = int(input(txt_to_display_when_delete)) - 1
    if prod_num_to_delete <= len(list_a) - 1 and prod_num_to_delete >= 0:
        list_a.pop(prod_num_to_delete)
    print(f'Products list: {list_a}')

if len(list_a):
    prod_num_to_delete = int(input(txt_to_display_when_delete)) - 1
    if prod_num_to_delete <= len(list_a) - 1 and prod_num_to_delete >= 0:
        list_a.pop(prod_num_to_delete)
    print(f'Products list: {list_a}')

if len(list_a):
    prod_num_to_delete = int(input(txt_to_display_when_delete)) - 1
    if prod_num_to_delete <= len(list_a) - 1 and prod_num_to_delete >= 0:
        list_a.pop(prod_num_to_delete)
    print(f'Products list: {list_a}')


if len(list_a):
    print("Products list is NOT empty\n")
else:
    print("Products list is EMPTY\n")


new_prods = input('Write more products: ')
new_prods_list = new_prods.replace(', ', ',').split(',')

list_a.extend(new_prods_list)

print('Products list: ', list_a)
print('BYE!')

# ===================================================================================================================

# shopping_cart = []
# for _ in range(5):
# item = input("Enter an item: ")
# shopping_cart.append(item)

# print("Your current shopping cart:")
# print(shopping_cart)

# while len(shopping_cart) > 0:
# remove_choice = input("Do you want to remove an item from the cart? (yes/no): ").lower()

# if remove_choice == 'yes':

# removed_item = shopping_cart.pop(0)
# print(f"Removed {removed_item} from the cart.")
# print("Updated shopping cart:", shopping_cart)
#  else:
# break

# if not shopping_cart:
# print("Your shopping cart is empty.")
# else:
# print("Final Shopping Cart:", shopping_cart)
