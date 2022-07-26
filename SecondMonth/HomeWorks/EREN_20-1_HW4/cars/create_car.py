class Car:
    def __init__(self, title, model, weight, hp, nm, max_speed, color):
        self.title = title
        self.model = model
        self.weight = weight
        self.hp = hp
        self.nm = nm
        self.max_speed = max_speed
        self.color = color

    def start_engine(self):
        return f'Engine on {self.title} started. Model: {self.model}.'

    def stop_engine(self):
        return f'Engine on {self.title} stopped. Model: {self.model}.'

    def car_info(self):
        return f'{self.title},{self.model}, {self.weight},{self.hp}, {self.nm}, {self.max_speed}, {self.color}'
