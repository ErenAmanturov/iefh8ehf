# [Переслано от Алексей]
# #ДЗУрок1 Дэдлайн 07.07.2022 23 59:
# 1. Создать класс Person с атрибутами fullname, age, is_married
# 2. Добавить в класс Person метод introduce_myself, который бы распечатывал всю информацию о человеке
# 3. Создать класс Student наследовать его от класса Person и дополнить его атрибутом marks, который был бы словарем, где ключ это название урока, а значение - оценка.
# 4. Добавить метод в класс Student, который бы подсчитывал среднюю оценку ученика по всем предметам
# 5. Создать класс Teacher и наследовать его от класса Person, дополнить атрибутом experience.
# 6. Добавить в класс Teacher атрибут уровня класса salary
# 7. Также добавить метод в класс Teacher, который бы считал зарплату по следующей формуле: к стандартной зарплате прибавляется бонус 5% за каждый год опыта свыше 3х лет.
# 8. Создать объект учителя и распечатать всю информацию о нем и высчитать зарплату
# 9. Написать функцию create_students, в которой создается 3 объекта ученика, эти ученики добавляются в список и список возвращается функцией как результат.
# 10. Вызвать функцию create_students и через цикл распечатать всю информацию о каждом ученике с его оценками по каждому предмету. Также рассчитать его среднюю оценку по всем предметам.


class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        return f"Fullname:{self.fullname}" \
               f"Age:{self.age}" \
               f"Marry:{self.is_married}"


class Student(Person):
    def __init__(self, fullname: str, age: int, is_married: str, marks: dict):
        super().__init__(fullname, age, is_married)
        self.marks = marks.items()
        for k, v in self.marks:
            print(f"Lesson:{k} Mark:{v}")

    def average_marks(self, *mark):
        return sum(mark) / len(mark)


class Teacher(Person):

    salary = 30000

    def __init__(self, fullname: str, age: int, is_married: str, experience: int,):
        super().__init__(fullname, age, is_married)
        self.experience = experience


