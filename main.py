x = int(input("Введите количество элементов в списке: "))
num1 = []
i=0
for i in range (0,x):
    num1.append(int(input("Введи элемент списка:")))
print(num1)
num2=[i**2 for i in num1]
print("Квадраты элементов:",num2)

