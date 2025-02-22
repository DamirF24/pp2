def polygon_area(sides, length):
    area = (sides * length ** 2) / (4 * math.tan(math.pi / sides))
    return area

sides = int(input("Input number of sides: "))
length = float(input("Input the length of a side: "))
area = polygon_area(sides, length)
print(f"The area of the polygon is: {area}")
