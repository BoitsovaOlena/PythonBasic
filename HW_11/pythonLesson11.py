# Homework 11

# Створіть клас "Транспортний засіб" та підкласи "Автомобіль", "Літак", "Корабель",
# наслідувані від "Транспортний засіб". Наповніть класи атрибутами на свій розсуд.
# Створіть обʼєкти класів "Автомобіль", "Літак", "Корабель".

from pprint import pprint


class Vehicle:
    driving_force = None
    average_speed = None
    maximum_speed = None
    speed_measurement_units = None
    fuel_consumption = None
    fuel_measurement_units = None
    max_notrefueling_distance = None
    distance_measurement_units = None

    def __init__(
            self,
            average_speed,
            maximum_speed,
            fuel_consumption,
            fuel_measurement_units,
            max_notrefueling_distance,
            speed_measurement_units='км/г',
            driving_force='двигун',
            distance_measurement_units='км'
    ):
        self.driving_force = driving_force
        self.average_speed = average_speed
        self.maximum_speed = maximum_speed
        self.speed_measurement_units = speed_measurement_units
        self.fuel_consumption = fuel_consumption
        self.fuel_measurement_units = fuel_measurement_units
        self.max_notrefueling_distance = max_notrefueling_distance
        self.distance_measurement_units = distance_measurement_units

    def get_vehicle(self):
        """
        Returns an object containing the main characteristics of an object of this class.

        :return:
        :rtype: object
        """
        vehicle_characteristics = {
            'driving_force': self.driving_force,
            'average_speed': f'{self.average_speed} {self.speed_measurement_units}',
            'maximum_speed': f'{self.maximum_speed} {self.speed_measurement_units}',
            'fuel_consumption': f'{self.fuel_consumption} {self.fuel_measurement_units}',
            'max_notrefueling_distance': f'{self.max_notrefueling_distance} {self.distance_measurement_units}'
        }
        return vehicle_characteristics

    def get_distance(self, time):
        """
        The function calculates the distance the vehicle will travel in a given time.
        :param time: Time in hours.
        :type time: int
        :return:
        :rtype: str|None
        """
        if isinstance(time, int):
            distance = time*self.average_speed
            return f'{distance} {self.distance_measurement_units}'
        return None


class Car(Vehicle):
    length = None
    width = None
    height = None
    wheel_base = None
    __units = 'см'

    def __init__(
            self,
            length,
            width,
            height,
            wheel_base,
            average_speed,
            maximum_speed,
            fuel_consumption,
            fuel_measurement_units,
            max_notrefueling_distance,
            speed_measurement_units='км/г',
            driving_force='двигун',
            distance_measurement_units='км',

    ):
        Vehicle.__init__(
            self,
            average_speed,
            maximum_speed,
            fuel_consumption,
            fuel_measurement_units,
            max_notrefueling_distance,
            speed_measurement_units,
            driving_force,
            distance_measurement_units
        )

        self.length = length
        self.width = width
        self.height = height
        self.wheel_base = wheel_base

    def get_vehicle(self):
        """
        Returns an object containing the main characteristics of an object of this class.

        :return:
        :rtype: object
        """
        vehicle_characteristics = {
            'driving_force': self.driving_force,
            'average_speed': f'{self.average_speed} {self.speed_measurement_units}',
            'maximum_speed': f'{self.maximum_speed} {self.speed_measurement_units}',
            'fuel_consumption': f'{self.fuel_consumption} {self.fuel_measurement_units}',
            'max_notrefueling_distance': f'{self.max_notrefueling_distance} {self.distance_measurement_units}',
            'dimensions':
                f'Довжина - {self.length}{self.__units}, '
                f'ширина - {self.width} {self.__units}, '
                f'висота - {self.height} {self.__units}.',
            'wheel_base': f'{self.wheel_base} {self.__units}'
        }
        return vehicle_characteristics


my_car = Car(average_speed=60,
             maximum_speed=200,
             fuel_consumption=10,
             fuel_measurement_units='л/100км',
             max_notrefueling_distance=500,
             length=400,
             width=200,
             height=130,
             wheel_base=300
             )
print('*************************************************')
print('my_car')
pprint(my_car.get_vehicle())
print('*************************************************')


class Ship(Vehicle):
    sediment = None
    __sediment_units = 'футів'
    buoyancy = None
    __buoyancy_units = '%'

    def __init__(
            self,
            sediment,
            buoyancy,
            average_speed,
            maximum_speed,
            fuel_consumption,
            fuel_measurement_units,
            max_notrefueling_distance,
            speed_measurement_units='вузлів',
            driving_force='двигун',
            distance_measurement_units='км',

    ):
        Vehicle.__init__(
            self,
            average_speed,
            maximum_speed,
            fuel_consumption,
            fuel_measurement_units,
            max_notrefueling_distance,
            speed_measurement_units,
            driving_force,
            distance_measurement_units
        )

        self.sediment = sediment
        self.buoyancy = buoyancy

    def get_vehicle(self):
        """
        Returns an object containing the main characteristics of an object of this class.

        :return:
        :rtype: object
        """
        vehicle_characteristics = {
            'driving_force': self.driving_force,
            'average_speed': f'{self.average_speed} {self.speed_measurement_units}',
            'maximum_speed': f'{self.maximum_speed} {self.speed_measurement_units}',
            'fuel_consumption': f'{self.fuel_consumption} {self.fuel_measurement_units}',
            'max_notrefueling_distance': f'{self.max_notrefueling_distance} {self.distance_measurement_units}',
            'sediment': f'Осадка судна - {self.sediment} {self.__sediment_units }.',
            'buoyancy': f'Плавучысть судна - {self.buoyancy} {self.__buoyancy_units }'
        }
        return vehicle_characteristics

    def get_distance(self, time):
        """
        The function calculates the distance the vehicle will travel in a given time.
        :param time: Time in hours.
        :type time: int
        :return:
        :rtype: str|None
        """
        if isinstance(time, int):
            distance = time*self.average_speed*1.835
            return f'{distance} {self.distance_measurement_units}'
        return None


my_ship = Ship(average_speed=50,
               maximum_speed=100,
               fuel_consumption=50,
               fuel_measurement_units='л/100км',
               max_notrefueling_distance=600,
               sediment=5,
               buoyancy=25
               )


print('my_ship')
pprint(my_ship.get_vehicle())
print('*************************************************')


class Plane(Vehicle):
    max_height = None
    __units = 'м'

    def __init__(
            self,
            max_height,
            average_speed,
            maximum_speed,
            fuel_consumption,
            fuel_measurement_units,
            max_notrefueling_distance,
            speed_measurement_units='км/г',
            driving_force='двигун',
            distance_measurement_units='км',

    ):
        Vehicle.__init__(
            self,
            average_speed,
            maximum_speed,
            fuel_consumption,
            fuel_measurement_units,
            max_notrefueling_distance,
            speed_measurement_units,
            driving_force,
            distance_measurement_units
        )

        self.max_height = max_height

    def get_vehicle(self):
        """
        Returns an object containing the main characteristics of an object of this class.

        :return:
        :rtype: object
        """
        vehicle_characteristics = {
            'driving_force': self.driving_force,
            'average_speed': f'{self.average_speed} {self.speed_measurement_units}',
            'maximum_speed': f'{self.maximum_speed} {self.speed_measurement_units}',
            'fuel_consumption': f'{self.fuel_consumption} {self.fuel_measurement_units}',
            'max_notrefueling_distance': f'{self.max_notrefueling_distance} {self.distance_measurement_units}',
            'max_height': f'Максимальна висота, на яку може піднятися літак - {self.max_height}{self.__units }.',
        }
        return vehicle_characteristics


my_plane = Plane(average_speed=50,
                 maximum_speed=100,
                 fuel_consumption=50,
                 fuel_measurement_units='л/100км',
                 max_notrefueling_distance=600,
                 max_height=3000
                 )


print('my_plane')
pprint(my_plane.get_vehicle())
print('*************************************************')
