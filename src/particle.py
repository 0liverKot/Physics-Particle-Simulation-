import arcade

class Particle:
    def __init__(self, x, y, radius, color, x_velocity, y_velocity, screen_width, screen_height):

        self.x = x
        self.y = y
        self.radius = radius
        self.color = color 
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity
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