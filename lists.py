#Задание 1 Списки

num = [3, 5, 7, 9, 10.5] #Создайте список из чисел 3, 5, 7, 9 и 10.5
print(num) #Выведите содержимое списка на экран
num.append('Python') #Добавьте в конец списка строку "Python"
print(num)
count = len(num) #Выведите длину списка на экран
print(count)

#Задание 2 Списки

print(num[0]) #Выведите на экран начальный элемент списка
print(num[-1]) #Выведите на экран последний элемент списка
print(num[2:5]) #Напечатайте элементы списка со второго по четвертый включительно
del num[-1] #Удалите из списка строку "Python"
print(num)
