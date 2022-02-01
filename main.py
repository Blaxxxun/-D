# Решение квадратных уровнений
print('a*x²+b*x+c')
a = input('a: ')
b = input('b: ')
c = input('c: ')

while True:
    try:
        a = float(a)
        b = float(b)
        c = float(c)
        break
    except:
        print("Неверное значение. Повторите попытку.")
        a = input('a: ')
        b = input('b: ')
        c = input('c: ')

d = b ** 2 - 4 * a * c

if d < 0:
    print('Корней нет')
elif d == 0:
    x = -b / (2 * a)
    print('x = ' + str(x))
else:
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    print('x₁ = ' + str(x1))
    print('x₂ = ' + str(x2))
