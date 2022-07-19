class Car:

    def __init__(self, model, engine, hp, max_speed, nm):
        self.model = model
        self.engine = engine
        self.hp = hp
        self.max_speed = max_speed
        self.nm = nm

    def start_engine(self):
        print(f'Engine on {self.model} started')

    def stop_engine(self):
        print(f'Engine on {self.model} stopped')


""" instance Car """
bmw = Car('i8', 'w8', '800', '300', '1100')
bmw.start_engine()
bmw.stop_engine()
