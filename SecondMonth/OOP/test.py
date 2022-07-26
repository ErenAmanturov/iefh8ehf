# a = 'a_a'
# a = a[0] + a[1:].title()
# print(a)
# (123) 456-7890
# a = [1, 3, 4, 3,5 ,4, 6,5, 7,7, 7]
# a = str(a)
# print(a)
# def dna_to_rna(dna):
#     for i in dna:
#         dna = i.replace('T', 'U')
#     return dna
#
#
# print(dna_to_rna('TTTT'))
x=int(input())
for i in range(x):
    print('%s%s' % (' ' * (x-i-1), '*' * (i*2+1)))
