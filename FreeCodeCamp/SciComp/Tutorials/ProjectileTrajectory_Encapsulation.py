import math

GRAVITATIONAL_ACCELERATION = 9.81
PROJECTILE = "∙"
x_axis_tick = "T"
y_axis_tick = "⊣"

class Projectile:
    __slots__ = ('__speed', '__height', '__angle')

    def __init__(self, speed, height, angle):
        self.__speed = speed
        self.__height = height
        self.__angle = math.radians(angle)

    def __calculate_displacement(self):
        horizontal_component = self.__speed * math.cos(self.__angle)
        vertical_component = self.__speed * math.sin(self.__angle)
        squared_component = vertical_component**2
        gh_component = 2 * GRAVITATIONAL_ACCELERATION * self.__height
        sqrt_component = math.sqrt(squared_component + gh_component)
        
        return horizontal_component * (vertical_component + sqrt_component) / GRAVITATIONAL_ACCELERATION

    def __str__(self):
        title = f'\nProject details:\n'
        speed = f'speed: {self.__speed} m/s\n'
        height = f'height: {self.__height} m\n'
        angle = f'angle: {int(math.degrees(self.__angle))}\N{DEGREE SIGN}\n'
        displace = f'displacement: {self.__calculate_displacement():.1f} m\n'
        return title + speed + height + angle + displace
    
    def __calculate_y_coordinate(self, x):
        height_component = self.__height
        angle_component = math.tan(self.__angle) * x
        acceleration_component = GRAVITATIONAL_ACCELERATION * x**2 / (
                2 * self.__speed**2 * math.cos(self.__angle)**2)
        y_coordinate = height_component + angle_component - acceleration_component

        return y_coordinate
    
    def calculate_all_coordinates(self):
        retList = []
        for x in range(math.ceil(self.__calculate_displacement())):
            retList.append((x, self.__calculate_y_coordinate(x)))
        return retList

    @property
    def height(self):
        return self.__height

    @property
    def angle(self):
        return round(math.degrees(self.__angle))

    @property
    def speed(self):
        return self.__speed
    
    @speed.setter
    def speed(self, new_value):
        self.__speed = new_value
    
    @height.setter
    def height(self, new_value):
        self.__height = new_value

    @angle.setter
    def angle(self, new_value):
        self.__angle = math.radians(new_value)



ball = Projectile(10, 3, 5)
print(ball)
coordinates = ball.calculate_all_coordinates()