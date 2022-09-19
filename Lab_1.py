import sys
import math

def get_coef(index, prompt):
    '''
    Читаем коэффициент из командной строки или вводим с клавиатуры
    Args:
        index (int): Номер параметра в командной строке
        prompt (str): Приглашение для ввода коэффицента
    Returns:
        float: Коэффициент квадратного уравнения
    '''
    try:
        # Пробуем прочитать коэффициент из командной строки
        coef_str = sys.argv[index]
    except:
        # Вводим с клавиатуры
        print(prompt)
        coef_str = input()
    try:
        float(coef_str)
        return float(coef_str)
    except:
        pass
    # Переводим строку в действительное число
    while True:
        try:
            print("Введен неверный аргумент под номером ",index)
            coef_str = input()
            float(coef_str)
            break
        except:
            pass
    return float(coef_str)


def get_roots(a, b, c):
    '''
    Вычисление корней квадратного уравнения
    Args:
        a (float): коэффициент А
        b (float): коэффициент B
        c (float): коэффициент C
    Returns:
        list[float]: Список корней
    '''
    if a == 0 and b != 0:
        return [-c/b]
    if a == 0:
        return []
    result = []
    D = b*b - 4*a*c
    if D == 0.0:
        root = -b / (2.0*a)
        result.append(root)
    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0*a)
        root2 = (-b - sqD) / (2.0*a)
        result.append(root1)
        result.append(root2)
    return result


def main():
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    # Вычисление корней
    roots = get_roots(a,b,c)
    len_roots = len(roots)
    if len_roots == 0:
        print(f"Нет корней")
    if len_roots == 1 and roots[0] >= 0:
        if roots[0] == 0:
            print("Корень: 0")
            exit()
        print(f"Корни: {math.sqrt(roots[0])}, {-math.sqrt(roots[0])}")
    if len_roots == 2:
        roots = list(filter(lambda x: x>= 0,roots))
        print("Корни: ")
        for i in roots:
            if i == 0:
                print(0,end = ',')
                continue
            print(math.sqrt(i),end = ',')
            print(-math.sqrt(i), end = ',')

# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()

# Пример запуска
# qr.py 1 0 -4