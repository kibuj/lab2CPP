import csv
import math

def get_rectangle_type(length, width):
    if length == width:
        return "Квадрат"
    return "Прямокутник"

def get_triangle_type(a, b, c):
    a, b, c = sorted([float(a), float(b), float(c)])
    if a == b == c:
        return "Рівносторонній трикутник"
    elif a == b or b == c or a == c:
        return "Рівнобедрений трикутник"
    elif math.isclose(a**2 + b**2, c**2, rel_tol=1e-9):
        return "Прямокутний трикутник"
    else:
        return "Звичайний трикутник"

def rectangle_area(length, width):
    return float(length) * float(width)

def rectangle_perimeter(length, width):
    return 2 * (float(length) + float(width))

def triangle_area(a, b, c):
    s = (float(a) + float(b) + float(c)) / 2
    return math.sqrt(s * (s - float(a)) * (s - float(b)) * (s - float(c)))

def triangle_perimeter(a, b, c):
    return float(a) + float(b) + float(c)

def process_shapes_from_csv(filename):
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            shape_type = row[0].lower()

            if shape_type == "прямокутник":
                length, width = map(float, row[1:3])
                if length <= 0 or width <= 0:
                    continue
                area = rectangle_area(length, width)
                perimeter = rectangle_perimeter(length, width)
                rect_type = get_rectangle_type(length, width)
                print(f"{rect_type}:")
                print(f"  Площа: {area:.2f}")
                print(f"  Периметр: {perimeter:.2f}")
            elif shape_type == "трикутник":
                a, b, c = map(float, row[1:4])
                if a <= 0 or b <= 0 or c <= 0 or (a + b <= c) or (a + c <= b) or (b + c <= a):
                    continue
                area = triangle_area(a, b, c)
                perimeter = triangle_perimeter(a, b, c)
                tri_type = get_triangle_type(a, b, c)
                print(f"{tri_type}:")
                print(f"  Площа: {area:.2f}")
                print(f"  Периметр: {perimeter:.2f}")
            else:
                continue
            print("-" * 30)




process_shapes_from_csv('CSVfile.csv')
