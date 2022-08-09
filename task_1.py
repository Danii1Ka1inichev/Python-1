a = lambda x, y: print(x**y)
try:
    print('Введите основание степени')
    x = int(input())
    print('Введите показатель степени')
    y = int(input())
    a(x,y)
except ValueError:
    print('Некорректный ввод')