import arcade
import random 

class Particle:
    def __init__(self, x, y,  screen_width, screen_height, radius='random', velocities='random', color='random'):

        def get_random_velocities(min, max):
            x_vel = random.randint(min, max)
            y_vel = random.randint(min, max)
            return (x_vel, y_vel)

        def get_random_radius(min, max):
            return random.randint(min, max)

        def get_random_color():
            return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        min_velocity = 1
        max_velocity = 10

        min_radius = 5
        max_radius = 20

        self.x = x
        self.y = y

        if radius == 'random':
            self.radius = get_random_radius(min_radius, max_radius)
        else:
            self.radius = radius

        if color == 'random':
            self.color = get_random_color()
        else:
            self.color = color
         
        if velocities == 'random':
            self.x_velocity, self.y_velocity = get_random_velocities(min_velocity, max_velocity)
        else:
            self.x_velocity, self.y_velocity = velocities

    
        self.screen_width = screen_width
        self.screen_height = screen_height

    def move(self):

        self.x += self.x_velocity
        self.y += self.y_velocity

        if self.x > self.screen_width - self.radius: 
            self.x_velocity *= -1
        elif self.x < 0 + self.radius: 
            self.x_velocity *= -1

        if self.y > self.screen_height - self.radius: 
            self.y_velocity *= -1
        elif self.y < 0 + self.radius: 
            self.y_velocity *= -1

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.radius, self.color)