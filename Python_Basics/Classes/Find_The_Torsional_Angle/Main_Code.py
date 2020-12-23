# Link: https://www.hackerrank.com/challenges/class-2-find-the-torsional-angle/problem

Input = '''
0 4 5
1 7 6
0 5 9
1 7 2
'''
Output = '8.19'

import math


class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        result_x = self.x - no.x
        result_y = self.y - no.y
        result_z = self.z - no.z
        return Points(result_x, result_y, result_z)

    def dot(self, no):
        result = self.x*no.x + self.y*no.y + self.z*no.z
        return result

    def cross(self, no):
        result_x = self.y * no.z - no.y * self.z
        result_y = -(self.x * no.z - no.x * self.z)
        result_z = self.x * no.y - no.x * self.y
        return Points(result_x, result_y, result_z)

    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)


if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    # *points[0] means assign every element in the list [0, 4, 5] to the class.
    # Without the *, the Points class will take the whole list [0, 4, 5] as 1 parameter only.
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))