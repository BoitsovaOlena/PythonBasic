# Homework 12

# 1. Доопрацюйте класс Line так, щоб в атрибути begin та end обʼєктів цього класу можна було записати
# тільки обʼєкти класу Point. Використовуйте property
# 2. Створіть класс Triangle (трикутник), який задається трьома точками (обʼєкти классу Point).
# Реалізуйте перевірку даних, аналогічно до класу Line. Визначет атрибут,
# що містить площу трикутника (за допомогою property). Для обчислень можна використати формулу Герона.

class Point:
    _x = None
    _y = None

    @property  # getter
    def x(self) -> int | None:
        return self._x

    @x.setter
    def x(self, value: int):
        if not isinstance(value, int):
            raise TypeError
        self._x = value

    @property  # getter
    def y(self) -> int | None:
        return self._y

    @y.setter
    def y(self, value: int):
        if not isinstance(value, int):
            raise TypeError
        self._y = value

    def __init__(self, x_coord, y_coord):
        self.x = x_coord
        self.y = y_coord


point1 = Point(3, 0)
point2 = Point(0, 4)
point3 = Point(3, 4)


class Line:
    _begin = None
    _end = None
    __error_message = \
        'To create an object of the Line class, an object of the Point class must be passed as an argument.'

    @property
    def begin(self) -> Point | None:
        return self._begin

    @begin.setter
    def begin(self, value: Point):
        if not isinstance(value, Point):
            raise TypeError(self.__error_message)
        self._begin = value

    @property
    def end(self) -> Point | None:
        return self._end

    @end.setter
    def end(self, value: Point):
        if not isinstance(value, Point):
            raise TypeError(self.__error_message)
        self._end = value

    def __init__(self, begin_point: Point, end_point: Point):
        self.begin = begin_point
        self.end = end_point

    @property
    def length(self) -> int | float:
        return ((self.begin.x - self.end.x) ** 2 + (self.begin.y - self.end.y) ** 2) ** 0.5


line1 = Line(point2, point1)

print('Line1 length: ', line1.length)


class Triangle:
    _vertex1 = None
    _vertex2 = None
    _vertex3 = None
    __error_message = \
        'To create an object of the Triangle class, an object of the Point class must be passed as an argument.'

    @property
    def vertex1(self) -> Point | None:
        return self._vertex1

    @vertex1.setter
    def vertex1(self, value: Point):
        if not isinstance(value, Point):
            raise TypeError(self.__error_message)
        self._vertex1 = value

    @property
    def vertex2(self) -> Point | None:
        return self._vertex2

    @vertex2.setter
    def vertex2(self, value: Point):
        if not isinstance(value, Point):
            raise TypeError(self.__error_message)
        self._vertex2 = value

    @property
    def vertex3(self) -> Point | None:
        return self._vertex3

    @vertex3.setter
    def vertex3(self, value: Point):
        if not isinstance(value, Point):
            raise TypeError(self.__error_message)
        self._vertex3 = value

    def __init__(self, vertex1: Point, vertex2: Point, vertex3: Point):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.vertex3 = vertex3

    @property
    def area(self):
        """
        The function calculates the area of a triangle using the coordinates of its vertices.
        Heron's formula is used.
        :return:
        :rtype: int|float
        """
        side1 = Line(self.vertex1, self.vertex2).length
        side2 = Line(self.vertex2, self.vertex3).length
        side3 = Line(self.vertex3, self.vertex1).length
        semi_perimeter = (side1 + side2 + side3) / 2
        return (semi_perimeter * (semi_perimeter - side1) * (semi_perimeter - side2) * (semi_perimeter - side3)) ** 0.5

    # Альтернативний варіант якщо у нас немає классу Line
    # @staticmethod
    # def side_length(point_1, point_2):
    #     """
    #     The function accepts 2 points, and based on their coordinates,
    #     calculates the length of the segment between them.
    #     :param point_1:
    #     :type point_1: Point
    #     :param point_2:
    #     :type point_2: Point
    #     :return: The length of the side.
    #     :rtype: int|float
    #     """
    #     return ((point_1.x - point_2.x) ** 2 + (point_1.y - point_2.y) ** 2) ** 0.5
    #
    # @property
    # def area(self):
    #     """
    #     The function calculates the area of a triangle using the coordinates of its vertices.
    #     Heron's formula is used.
    #     :return:
    #     :rtype: int|float
    #     """
    #     side1 = self.side_length(self.vertex1, self.vertex2)
    #     side2 = self.side_length(self.vertex2, self.vertex3)
    #     side3 = self.side_length(self.vertex3, self.vertex1)
    #     semi_perimeter = (side1 + side2 + side3) / 2
    #     return (semi_perimeter * (semi_perimeter - side1) * (semi_perimeter - side2) * (semi_perimeter - side3)) ** 0.5


triangle = Triangle(point1, point2, point3)

print('Triangle area: ', triangle.area)
