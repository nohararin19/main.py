import turtle


class Spaceship:
    turtle.screensize(2000, 1100)
    turtle.title("MOBB, Мамлютов, Отеген, Бейсек, Битанов")  # фон, маркер
    turtle.bgpic("frame1.gif")
    shuttle_roof_color = '#B0C4DE'
    shuttle_main_color = '#C0C0C0'
    f = turtle.Turtle()
    f.shape("turtle")
    f.pensize(4)
    f.pencolor('black')
    i = 0

    def up(self):
        Spaceship.f.up()
        y = Spaceship.f.ycor() + 10
        Spaceship.f.sety(y)
        Spaceship.f.setheading(90)
        Spaceship.f.down()

    def down(self):
        Spaceship.f.up()
        y = Spaceship.f.ycor() - 10
        Spaceship.f.sety(y)
        Spaceship.f.setheading(270)
        Spaceship.f.down()

    def left(self):
        Spaceship.f.up()
        x = Spaceship.f.xcor() - 10
        Spaceship.f.setx(x)
        Spaceship.f.setheading(180)
        Spaceship.f.down()

    def right(self):
        Spaceship.f.up()
        x = Spaceship.f.xcor() + 10
        Spaceship.f.setx(x)
        Spaceship.f.setheading(360)
        Spaceship.f.down()
        Spaceship.i += 1
        if Spaceship.i == 5:
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
