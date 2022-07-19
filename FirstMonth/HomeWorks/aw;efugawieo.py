def f(a, *args, **kwargs):
 print('{} | {} | {}'.format(a, args, kwargs))


f(1, 2, 3, x=4, y=5 )
