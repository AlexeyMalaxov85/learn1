#Задание 1 Словари

temp = {'city': 'Москва', 'temperature': 20} #Создайте словарь
print(temp['city']) #Выведите на экран значение ключа city

temp['temperature'] = temp['temperature'] - 5 #Уменьшите значение "temperature" на 5  

print(temp) #Выведите на экран весь словарь

#Задание 2 Словари

print(temp.get('country', 'Россия')) #Проверьте, есть ли в словаре ключ country
                                     #Выведите значение по-умолчанию "Россия" для ключа country
temp.setdefault('date', '27.05.2019') #Добавьте в словарь элемент date со значением "27.05.2019"
print(temp)
print(len(temp)) #Выведите на экран длину словаря
