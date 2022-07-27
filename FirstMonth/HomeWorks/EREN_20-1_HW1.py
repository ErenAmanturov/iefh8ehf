chui = float(input('Введите температуру Чуйской области на сегодня:'))

batken = float(input('Введите температуру Баткенской области на сегодня:'))

issikkul = float(input('Введите температуру Иссык-кульской области на сегодня:'))

jalalabad = float(input('Введите температуру Джалал-Абадской области на сегодня:'))

naryn = float(input('Введите температуру Нарынской области на сегодня:'))

talas = float(input('Введите температуру Талаской области на сегодня:'))

osh = float(input('Введите температуру Ошской области на сегодня: '))


sumtemp = chui + batken + issikkul + jalalabad + naryn + talas + osh

averageage = sumtemp / 7

averageage = round(averageage, 1)

print('Средний показатель температуры воздуха по КР на сегодня', averageage, "°C")
