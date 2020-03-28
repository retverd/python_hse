# Напишите программу, которая будет разрезать большую прямоугольную область на N × N одинаковых прямоугольных
# областей. Области задаются четырьмя координатами: минимальной широтой, минимальной долготой, максимальной широтой,
# максимальной долготой.
#
# При выводе области должны быть упорядочены по возрастанию минимальной широты, а в случае равных широт - по возрастанию
# минимальной долготы.
#
# Гарантируется, что все числа во входных данных положительны.

coords = list(map(float, input().split()))
n = int(input())

lat_step = (coords[2] - coords[0]) / n
lon_step = (coords[3] - coords[1]) / n

for lat_i in range(n):
    min_lat = coords[0] + lat_step * lat_i
    max_lat = coords[0] + lat_step * (lat_i + 1)
    for lon_i in range(n):
        min_lon = coords[1] + lon_step * lon_i
        max_lon = coords[1] + lon_step * (lon_i + 1)

        print(min_lat, min_lon, max_lat, max_lon)
