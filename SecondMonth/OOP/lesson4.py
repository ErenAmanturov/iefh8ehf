# import testmodule
# testmodule.say_hello('Eren')
# print(testmodule.ts)

# from testmodule import say_hello, ts
#
# say_hello('Eren')
# print(ts)

# import math
# import datetime
# from colorama import Back, Fore, Style
# print(Fore.BLUE, Style.BRIGHT, Back.GREEN, 'Almaz Goluboi')

from person.create_person import create_person

jack = create_person('Jack', 'Barbaro', 21)
print(jack.get_full_name())
