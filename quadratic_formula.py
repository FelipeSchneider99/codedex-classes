print('Quadratic Formula Solver!')

a = float(input('Enter coefficient a: '))
b = float(input('Enter coefficient b: '))
c = float(input('Enter coefficient c: '))
delta = b**2 -4*a*c
if delta < 0:
    print('No real roots exist.')
elif delta == 0:
    root = -b / (2*a)
    print('One real root exists:', root)
else:
    root1 = (-b + delta**0.5) / (2*a)
    root2 = (-b - delta**0.5) / (2*a)
    print('Two real roots exist:', root1, 'and', root2)