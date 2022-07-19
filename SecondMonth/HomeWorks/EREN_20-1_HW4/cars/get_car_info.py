from .create_car import Car


def get_car_info(title,model, weight, hp, nm, max_speed, color):
    car = Car (
            title=title,
            model=model,
            weight=weight,
            hp=hp,
            nm=nm,
            max_speed=max_speed,
            color=color
    )
    return car
