class Car:
#2u3riu2r
    def __init__(self, title, model, weight, hp, nm, max_speed, color):
        self.title = title
        self.model = model
        self.weight = weight
        self.hp = hp
        self.nm = nm
        self.max_speed = max_speed
        self.color = color

    def start_engine(self):
        print(f'Engine on {self.title} started. Model: {self.model}.')

    def stop_engine(self):
        print(f'Engine on {self.title} stopped. Model: {self.model}.')

    def info(self):
        print(f'Title: {self.title}\nModel: {self.model}\nWeight: {self.weight}\nHP: {self.hp}\nNM: {self.nm}\
        \nMaxSpeed: {self.max_speed}\nColor: {self.color}.')


bmw = Car('Bmw', 'i8', '1000 kg', 400, 100, 250, 'green')
bmw.start_engine()

bmw.stop_engine()
bmw.info()
