import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Art in Python")

artist = turtle.Turtle()
artist.speed("fastest")
artist.pensize(2)

def draw_petal(size, color_name):
    artist.color(color_name)
    artist.begin_fill()

    for _ in range(2):
        artist.circle(size, 60)
        artist.left(120)

    artist.end_fill()

colors = ["red", "orange", "yellow", "blue", "green", "purple", "violet"]

for i in range(36):
    draw_petal(90, colors[i % len(colors)])  # Fixed variable name
    artist.right(10)

artist.hideturtle()
screen.exitonclick()