import random
import turtle as t

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_col = (r, g, b)
    return random_col


for _ in range(72):
    tim.color(random_color())
    tim.circle(100)
    current_position = tim.heading()
    tim.setheading(current_position+5)


my_screeen = t.Screen()
my_screeen.exitonclick()
