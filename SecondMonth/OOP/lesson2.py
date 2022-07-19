
class Transport:

    def __init__(self, title, model, engine, ms, speed):
        self.title = title
        self.model = model
        self.engine = engine
        self.ms = ms
        self.speed = speed

    def start_engine(self):
        print(f'Engine on {self.title} {self.model} started')


class Car(Transport):

    _current_speed = 0

    def __init__(self, title, model, engine, ms, speed, color):
        super().__init__(title, model, engine, ms, speed)
        self.color = color

    def stop_engine(self):
        print(f'it stops engine in Car')

    def gas(self):
        if self._current_speed + self.speed >= self.ms:
            print('CHECK on')
        else:
            self._current_speed += self.speed
            print(self._current_speed)

    def stop(self):
        if self._current_speed - self.speed > 0:
            self._current_speed -= self.speed
        else:
            self._current_speed = 0
        print(self._current_speed)


class Airplane(Transport):

    def stop_engine(self):
        print(f'it stops engine in Airplane')


bmw = Car('bmw', 'i8', 'v10', 290, 60, 'black')
bmw.gas()
# bmw.start_engine()
# bmw.stop_engine()
boeing = Airplane('Boeing', '77', 'v100', 20000, 2000)
# boeing.start_engine()
# boeing.stop_engine()
