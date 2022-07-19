while True:
      date = input('Введите дату рождения: ')
      month = int(date[3:5])
      day = int(date[0:2])
      if day >= 21 and day <= 31 and month == 3 or month == 4 and day >= 1 and day <= 1:

          print('Овен')

      elif (day >= 20 and day <= 30 and month == 4) or(month == 5 and day >= 1 and day <= 20):

          print('Телец')

      elif (day >= 21 and day <= 31 and month == 5) or(month == 6 and day >= 1 and day <= 21):

          print('Близнецы')

      elif (day >= 22 and day <= 30 and month == 6) or(month == 7 and day >= 1 and day <= 22):

          print('Рак')

      elif (day >= 23 and day <= 31 and month == 7) or(month == 8 and day >= 1 and day <= 22):

          print('Лев')

      elif (day >= 23 and day <= 31 and month == 8) or(month == 9 and day >= 1 and day <= 22):

          print('Дева')

      elif (day >= 23 and day <= 30 and month == 9) or(month == 10 and day >= 1 and day <= 23):

          print('Весы')

      elif (day >= 24 and day <= 31 and month == 10) or(month == 11 and day >= 1 and day <= 22):

          print('Скорпион')``

      elif (day >= 23 and day <= 30 and month == 11) or(month == 12 and day >= 1 and day <= 21):

          print('Стрелец')

      elif (day >= 22 and day <= 31 and month == 12) or(month == 1 and day >= 1 and day <= 20):

          print('Козерог')

      elif (day >= 21 and day <= 31 and month == 1) or(month == 2 and day >= 1 and day <= 18):

          print('Водолей')

      elif (day >= 19 and day <= 29 and month == 2) or(month == 3 and day >= 1 and day <= 20):

          print('Рыбы')
      else:
          print('Подсказка:21.09')