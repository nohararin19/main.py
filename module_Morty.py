import turtle
skin_color = '#FFDEAD'
hair_color = '#8B4513'


class Morty:
    turtle.title("MOBB, Мамлютов, Отеген, Бейсек, Битанов")  # фон,
    turtle.bgpic("frame1.gif")
    m = turtle.Turtle()
    m.shape("turtle")
    m.pensize(4)
    m.pencolor('black')

    m.up()  # волосы
    m.goto(-400, -170)
    m.setheading(90)
    m.down()
    m.color('black', hair_color)
    m.begin_fill()
    m.circle(250, 180)
    m.left(90)
    m.forward(500)
    m.end_fill()

    m.up()  # лицо
    m.home()
    m.setheading(180)
    m.forward(650)
    m.down()
    m.color('black', skin_color)
    m.begin_fill()
    m.circle(200, 360)
    m.end_fill()

    m.up()  # глаза
    m.goto(-575, -100)
    m.down()
    m.color('black', 'white')
    m.begin_fill()
    m.circle(60, 360)
    m.up()
    m.forward(140)
    m.down()
    m.circle(60, 360)
    m.end_fill()
    m.up()
    m.left(90)
    m.forward(60)
    m.down()
    m.dot(10, 'black')
    m.up()
    m.left(90)
    m.forward(140)
    m.down()
    m.dot(10, 'black')

    m.up()  # уши
    m.goto(-455, -250)
    m.down()
    m.setheading(0)
    m.color('black', skin_color)
    m.begin_fill()
    m.circle(50, 180)
    m.left(90)
    m.forward(107)
    m.end_fill()
    m.right(90)
    m.up()
    m.goto(-850, -160)
    m.down()
    m.color('black', skin_color)
    m.begin_fill()
    m.circle(50, 195)
    m.end_fill()

    m.up()  # брови
    m.goto(-800, -140)
    m.down()
    m.left(35)
    m.forward(110)
    m.setheading(0)
    m.up()
    m.forward(150)
    m.down()
    m.left(315)
    m.forward(110)

    m.up()  # нос
    m.goto(-650, -250)
    m.down()
    m.forward(15)
    m.circle(15, 180)
    m.forward(15)

    m.up()  # рот
    m.goto(-650, -335)
    m.down()
    m.setheading(270)
    m.left(25)
    m.forward(15)
    m.circle(12, 180)
    m.forward(15)
    m.setheading(0)
    m.right(55)
    m.forward(25)
    m.circle(14, 180)
    m.forward(30)
