import re


class ValidCarNumber:

    def is_valid(self, number):
        isvalid = re.search(r'0([1-9]{1})KG(\d{3})([A-Z]{2,3})', number)
        try:
            if number[isvalid.start():isvalid.end()] == number:
                return f'Is valid number'
            elif number[isvalid.start():isvalid.end()] < number:
                return f'Is invalid number'
        except AttributeError:
            return f'Is invalid number'


bmw = ValidCarNumber()
print(bmw.is_valid('01KG777BAD'))
print(bmw.is_valid('hhh777hhh'))
