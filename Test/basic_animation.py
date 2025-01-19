import arcade 
import random 

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
SCREEN_TITLE = 'Animation'

MIN_CIRCLE_DIAMETER = 5
MAX_CIRCLE_DIAMETER = 25 

MIN_VELOCITY = 1
MAX_VELCOITY = 10

NUM_CIRCLES = 3000

class Circle:
    def __init__(self, x, y, diameter, color, x_velocity, y_velocity):

        self.x = x
        self.y = y
        self.diameter = diameter
        self.color = color 
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity

    def move(self):

        self.x += self.x_velocity
        self.y += self.y_velocity

        if self.x > SCREEN_WIDTH - self.diameter/2: 
            self.x_velocity *= -1
        elif self.x < 0 + self.diameter/2: 
            self.x_velocity *= -1

        if self.y > SCREEN_HEIGHT - self.diameter/2: 
            self.y_velocity *= -1
        elif self.y < 0 + self.diameter/2: 
            self.y_velocity *= -1

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.diameter/2, self.color)


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE) 

        self.circle_list = [] 

        for _ in range(NUM_CIRCLES):

            circle_diameter = get_circle_size(MIN_CIRCLE_DIAMETER, MAX_CIRCLE_DIAMETER)
            circle_position = get_random_position(SCREEN_WIDTH, SCREEN_HEIGHT, circle_diameter)
            circle_colour = get_circle_color()
            velocity = get_velocity(MIN_VELOCITY, MAX_VELCOITY)

            circle = Circle(circle_position[0], circle_position[1], circle_diameter, circle_colour, velocity[0], velocity[1])

            self.circle_list.append(circle)

    def on_update(self, dt): 

        for circle in self.circle_list:
            circle.move()

    def on_draw(self):

        self.clear()
        
        for circle in self.circle_list:
            circle.draw()


def get_random_position(screen_width, screen_height, circle_diameter):
    x = random.randint(0 + (circle_diameter//2), screen_width - (circle_diameter//2))
    y = random.randint(0 + (circle_diameter//2), screen_height - (circle_diameter//2))
    return [x, y]  


def get_circle_size(min_diameter, max_diameter): 
    return random.randint(min_diameter, max_diameter)


def get_circle_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def get_velocity(min_velocity, max_velocity):   
    return (random.randint(min_velocity, max_velocity), random.randint(min_velocity, max_velocity))


def main():
    MyGame()
    arcade.run()

if __name__ == "__main__":
    main()