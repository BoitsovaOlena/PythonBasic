class IsInteger:
    """
    The class is used to create objects that can only be int. When assigning other values, an error is raised.
    """
    @classmethod
    def verify_item(cls, item):
        if type(item) != int:
            raise TypeError('value must be integer')

    def __set_name__(self, owner, name: str):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_item(value)
        setattr(instance, self.name, value)


class IsString:
    """
    The class is used to create objects that can only be string. When assigning other values, an error is raised.
    """
    @classmethod
    def verify_item(cls, item):
        if type(item) != str:
            raise TypeError('value must be string')

    def __set_name__(self, owner, name: str):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_item(value)
        setattr(instance, self.name, value)


class IsFloat:
    """
    The class is used to create objects that can only be float. When assigning other values, an error is raised.
    """
    @classmethod
    def verify_item(cls, item):
        if type(item) != float:
            raise TypeError('value must be float')

    def __set_name__(self, owner, name: str):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_item(value)
        setattr(instance, self.name, value)


class Vehicle:
    producer = IsString()
    model = IsString()
    year = IsInteger()
    tank_capacity = IsFloat()
    tank_level = IsFloat()
    max_speed = IsInteger()
    fuel_consumption = IsFloat()
    odometer_value = IsInteger()

    def __init__(self, producer, model, year, tank_capacity, max_speed, fuel_consumption):
        self.producer = producer
        self.model = model
        self.year = year
        self.tank_capacity = tank_capacity
        self.tank_level = float(0)
        self.max_speed = max_speed
        self.fuel_consumption = fuel_consumption
        self.odometer_value = int(0)

    def __repr__(self):
        return f'ClassLib.Vehicle object.\nCar produced in {self.year} by {self.producer}, model {self.model}, ' \
               f'odometer {self.odometer_value}km.'

    def __eq__(self, other):
        if not isinstance(other, Vehicle):
            raise TypeError('An argument can only be another vehicle (object of the class Vehicle)')
        conditions = [
            self.year == other.year,
            self.odometer_value == other.odometer_value
        ]
        return all(conditions)

    @property
    def max_distance(self) -> int:
        return int(self.tank_level * 100 / self.fuel_consumption)

    def refueling(self):
        """
        When using this method, the car tank is filled to the maximum level.
        And the console displays a message about the amount of refueled fuel.
        :return:
        :rtype: None
        """
        tank_refueling = self.tank_capacity - self.tank_level
        self.tank_level = self.tank_capacity
        print(f'The car was filled with {tank_refueling} liters of fuel')

    def race(self, distance):
        """
        The function takes the distance and calculates the trip for the corresponding distance.
        The amount of necessary fuel and time are calculated, as well as the ability to overcome the
        given distance with the available fuel supply.
        :param distance: Race distance.
        :type distance: int
        :return: Dictionary containing distance, remaining fuel and race time.
        :rtype: dict
        """
        if not isinstance(distance, int):
            raise TypeError('The distance value must be an int')
        rase_distance = distance if self.max_distance > distance else self.max_distance
        total_fuel_consumption = (rase_distance*self.fuel_consumption)/100
        self.tank_level -= total_fuel_consumption
        self.odometer_value += rase_distance
        res = {
            'distance': rase_distance,
            'tank_level': self.tank_level,
            'race_time': rase_distance/(self.max_speed*0.8)
        }
        return res

    def lend_fuel(self, other):
        """
        The method is used for refueling from another vehicle.
        If the tank of the car on which the method was used is full a message
        'Sorry, my mistake, my tank is full.' is displayed.
        If the tank of another car is empty a message
        'That's OK, I'll figure it out somehow' is displayed.
        If refueling is possible, the amount of available fuel in both cars is adjusted and a message
        'Thanks bro, helped. You poured me {tank_refueling} liters of fuel' is displayed.
        :param other: Another vehicle.
        :type other: Vehicle
        :return:
        :rtype: None
        """
        if not isinstance(other, Vehicle):
            raise TypeError('An argument can only be another vehicle (object of the class Vehicle)')
        need_fuel = self.tank_capacity - self.tank_level
        available_fuel = other.tank_level
        if need_fuel == 0:
            print('Sorry, my mistake, my tank is full.')
        elif available_fuel == 0:
            print('That\'s OK, I\'ll figure it out somehow')
        else:
            tank_refueling = need_fuel if need_fuel < available_fuel else available_fuel
            self.tank_level += tank_refueling
            other.tank_level -= tank_refueling
            print(f'Thanks bro, helped. You poured me {tank_refueling} liters of fuel')
