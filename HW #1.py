import math

varieble_1 = 15
varieble_2 = 10
varieble_3 = 5

print(varieble_1 + varieble_2)
print(varieble_1 * varieble_2)
print(varieble_1 / varieble_2)
print(varieble_1 - varieble_2)

result = varieble_2 + varieble_1
print(result)
result = varieble_2 * varieble_1
print(result)
result = varieble_1 / varieble_2
print(result)
result = varieble_1 - varieble_2
print(result)

result = varieble_1 % varieble_3
print(result)

result = varieble_1 // varieble_3
print(result)

sample_text = "hello word"
print(sample_text)
print(type(sample_text))

sample_text_1 = "5"
sample_text_2 = "4"

print(sample_text_1)
print(type(sample_text_1))
print((sample_text_1 + sample_text_2))


sample_text_1_int = int(sample_text_1)
sample_text_2_int = int(sample_text_2)
result = (sample_text_2_int + sample_text_1_int)
print(result)


age = int(input("How old are you ?"))
print(age)
print(type(age))

name = input("Whats your name ?")
print(name)
print(type(name))


c = int(input("Enter degrees Celsius"))
f = ((c * 9) / 5) + 32
print(f"{c} degrees Celsius equals {f} degrees Fahrenheit")


f = int(input("Enter degrees Fahrenheit"))
c = ((c * 9) / 5) + 32
print(f"{c} degrees Fahrenheit equals {f} degrees Celsius")




n = int(input("Apples:"))
k = int(input("Pupils:"))
print(n % k, n // k)

n = int(input("Enter data"))
hours = n % (60 * 24) // 60
minutes = n % 60
print(hours, minutes)

a = input("a = ")
b = input("b = ")

a = float(a)
b = float(b)

area = (a * b) / 2

c = math.sqrt(a**2 + b**2)

perimeter = a + b + c

print("Area:", area)
print("Perimeter:", perimeter)


X = int(input())
Y = int(input())
Z = int(input())
A = 3
B = 5
C = 12
print(X*A+Y*B+Z*C)
