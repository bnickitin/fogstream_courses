#Длина Московской кольцевой автомобильной дороги —109 километров. Стартуем с нулевого километра МКАД и едем со скоростью V километров в час. На какой отметке остановимся через T часов? Программа получает на вход значение V и T. Если V>0, то движемся в положительном направлении по МКАД, если же значение V<0, то в отрицательном. Программа должна вывести целое число от 0 до 108 — номер отметки, на которой остановимся.
S = 109
print("введите скорость в 'км/ч' и нажмите enter")
V = float(input())
print("введите время в часах и нажмите enter")
t = float(input())
if V:
S = (V * t) % 108
print(S)
else:
print ("мы остались на месте")
