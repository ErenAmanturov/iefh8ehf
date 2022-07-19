import re

# email = "geektech@gmail.com"
# is_valid = re.search(r'.+[a-zA-Z\d]@(gmail|yandex|mail)\.(com|ru)', email)
#
# try:
#     if email[is_valid.start():is_valid.end()] == email:
#         print('It valid email')
# except AttributeError:
#     print('it Invalid email!')

"""

phone_number = +996-777-77-77-77
+
ISO_number = 996
operator_number = 777
-
77
-
77
-
77

"""

# phone = '+996-777-77-87-77'
# is_valid = re.search(r'\+996-(\d{3})-(\d{2})-(\d{2})-(\d{2})', phone)
#
# try:
#     if phone[is_valid.start():is_valid.end()] == phone:
#         print('Is valid number')
# except AttributeError:
#     print('IS invalid number')


