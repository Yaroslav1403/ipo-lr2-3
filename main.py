#Импортируем модуль math для использования математических функций
import math
#Просим пользователя ввести объём
V = float(input("Введите объем сферы: "))
#Радиус равен = формула
radius = (3 * V ** (1/3)) / (4 * math.pi)
#Вывод радиуса сферы
print(f"Радиус сферы: {radius:}")
