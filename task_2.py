a = lambda x, y, z: print(eval(f'{x}{z}{y}'))
try:
    print('Введите первое число')
    x = int(input())
    print('Введите второе число')
    y = int(input())
    print('Введите математическе действие(+-/*)')
    z = input()
    a(x, y, z)
except ValueError:
    print('Некорректный ввод числа')

except SyntaxError:
    print('Некорректный ввод математического действия')