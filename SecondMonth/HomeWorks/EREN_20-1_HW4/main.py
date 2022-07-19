from cars.get_car_info import get_car_info


bmw = get_car_info('bmw', 'i8', '2000kg', 200, 341, 300, 'light green')
print(bmw.start_engine())
print(bmw.stop_engine())
print(bmw.car_info())
