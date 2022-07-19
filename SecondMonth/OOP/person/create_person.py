from .models import Person


def create_person(first_name: str, last_name: str, age: int) -> Person:
    person = Person(
        first_name=first_name,
        last_name=last_name,
        age=age
    )

    return person
