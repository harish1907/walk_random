import random
import turtle as t

directions = [0, 90, 180, 270]
tim = t.Turtle()
tim.pensize(15)
tim.speed("fastest")
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_col = (r, g, b)
    return random_col


for _ in range(300):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))

my_screen = t.Screen()
my_screen.exitonclick()

