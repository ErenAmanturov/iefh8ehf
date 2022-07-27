"""

Data Structure

"""


"""

list, set, tuple - Data Structure

"""

"""

Linked List - 
what is?

"""
list_ = [1, 2, 3, 4, 5]

"""

Hash Table

"""

# user_age = {  # Hash Table
#     "Ali": 17,  # Hash function : Hash value
#     "Almaz": 17,
#     "Eren": 17,
#     "Aitegin": 17,
#     "Beka": 18,
#     "Abdurahim": 18,
#     "Azamat": 25
# }
#
# name = input('Name:')
# print(user_age[name])

"""

Big O(1)

"""

mass = [7, 3, 4, 8, -1, -2, 34, 24, 56, 23, 78]

"""

Big O(n*n)

"""

for i in range(len(mass)):
    for j in range(i, len(mass)):
        if mass[i] > mass[j]:
            mass[i], mass[j] = mass[j], mass[i]

print(mass)
