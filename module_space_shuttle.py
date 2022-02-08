import turtle


class Spaceship:
    turtle.title("MOBB, Мамлютов, Отеген, Бейсек, Битанов")  # фон, маркер
    turtle.bgpic("frame1.gif")
    shuttle_roof_color = '#B0C4DE'
    shuttle_main_color = '#C0C0C0'
    f = turtle.Turtle()
    f.shape("turtle")
    f.pensize(4)
    f.pencolor('black')

    def draw(self):
        Spaceship.f.up()  # космический шатл
        Spaceship.f.goto(800, 180)
        Spaceship.f.down()
        Spaceship.f.setheading(90)

        Spaceship.f.color('black', Spaceship.shuttle_main_color)
        Spaceship.f.begin_fill()
        Spaceship.f.circle(60, 90)
        Spaceship.f.forward(80)
        Spaceship.f.end_fill()
        Spaceship.f.setheading(90)
        Spaceship.f.color('black', Spaceship.shuttle_roof_color)
        Spaceship.f.begin_fill()
        Spaceship.f.circle(100, 180)
        Spaceship.f.end_fill()
        Spaceship.f.color('black', Spaceship.shuttle_main_color)
        Spaceship.f.begin_fill()
        Spaceship.f.right(90)
        Spaceship.f.forward(80)
        Spaceship.f.circle(60, 90)
        Spaceship.f.left(90)
        Spaceship.f.forward(480)

        Spaceship.f.up()
        Spaceship.f.goto(800, 180)
        Spaceship.f.down()
        Spaceship.f.setheading(90)
        Spaceship.f.circle(60, 90)
        Spaceship.f.forward(80)
        Spaceship.f.end_fill()
        Spaceship.f.setheading(90)
        Spaceship.f.end_fill()
