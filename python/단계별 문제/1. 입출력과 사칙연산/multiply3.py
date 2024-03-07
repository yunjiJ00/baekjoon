num1 = int(input())
num2 = int(input())
first = num2 % 10
second = (num2 % 100) // 10
third = num2 // 100
print(num1 * first)
print(num1 * second)
print(num1 * third)
print(num1 * num2)