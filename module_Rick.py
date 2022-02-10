import turtle


class Rick:
    turtle.screensize(2000, 1100)
    turtle.title("MOBB, Мамлютов, Отеген, Бейсек, Битанов")  # фон, маркер
    turtle.bgpic("frame1.gif")
    t = turtle.Turtle()
    t.shape("turtle")
    t.pensize(4)
    t.pencolor('black')

    t.penup()  # правый глаз
    t.forward(75)
    t.pendown()
    t.forward(70)
    t.left(110)
    t.forward(25)
    t.circle(30, 125)
    t.left(22)
    t.forward(34)
    t.left(25)
    t.forward(30)
    t.circle(30, 150)
    t.left(13)
    t.forward(40)

    t.up()  # зрачок
    t.left(98)
    t.forward(30)
    t.down()
    t.color('black', 'black')
    t.begin_fill()
    t.circle(4, 360)
    t.end_fill()

    t.up()  # левый глаз
    t.forward(160)
    t.down()
    t.setheading(0)
    t.forward(70)
    t.left(110)
    t.forward(25)
    t.circle(30, 125)
    t.left(22)
    t.forward(34)
    t.left(25)
    t.forward(30)
    t.circle(30, 150)
    t.left(13)
    t.forward(40)

    t.up()  # зрачок
    t.left(98)
    t.forward(30)
    t.down()
    t.color('black', 'black')
    t.begin_fill()
    t.circle(4, 360)
    t.end_fill()

    t.up()  # лицо
    t.forward(110)
    t.down()
    t.left(90)
    t.forward(180)
    t.circle(150, 180)
    t.left(1)
    t.forward(230)
    t.circle(150, 150)
    t.left(22)
    t.forward(120)

    t.up()  # левое ухо
    t.forward(75)
    t.right(90)
    t.down()
    t.forward(25)
    t.circle(25, 180)
    t.left(340)
    t.forward(50)

    t.up()  # правое ухо
    t.setheading(0)
    t.forward(300)
    t.down()
    t.left(25)
    t.forward(50)
    t.circle(25, 155)
    t.forward(45)

    t.up()  # рот
    t.forward(200)
    t.left(90)
    t.forward(100)
    t.down()
    t.color('black')
    t.begin_fill()
    t.forward(10)
    t.left(90)
    t.forward(150)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(150)
    t.end_fill()
    t.up()
    t.right(90)
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.down()
    for i in range(2):
        t.left(65)
        t.forward(35)
    t.setheading(0)
    t.up()
    t.forward(180)
    t.down()
    for i in range(2):
        t.left(65)
        t.forward(35)
    t.setheading(180)
    t.up()
    t.forward(40)
    t.left(90)
    t.forward(30)
    t.down()
    t.color('black', '#07e63f')
    t.begin_fill()
    t.forward(35)
    t.right(34)
    t.forward(20)
    t.left(34)
    t.forward(25)
    t.setheading(90)
    t.left(90)
    t.forward(10)
    t.right(45)
    t.forward(50)
    t.setheading(90)
    t.forward(40)
    t.end_fill()

    t.up()  # нос
    t.forward(120)
    t.left(90)
    t.forward(15)
    t.down()
    t.left(90)
    t.forward(65)
    t.circle(20, 180)
    t.forward(65)

    t.up()  # бровь
    t.forward(180)
    t.right(90)
    t.forward(50)
    t.down()
    t.color('black', '#00BFFF')
    t.begin_fill()
    t.setheading(270)
    t.right(90)
    t.forward(25)
    t.left(90)
    t.forward(5)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(5)
    t.left(90)
    t.forward(55)
    t.circle(15, 180)
    t.right(20)
    t.forward(15)
    t.setheading(0)
    t.forward(125)
    t.left(25)
    t.forward(45)
    t.circle(10, 160)
    t.end_fill()

    t.up()
    t.setheading(0)
    t.forward(77)
    t.right(90)
    t.forward(320)
    t.setheading(0)
    t.down()
    t.left(55)
    t.forward(175)
    t.left(90)
    t.forward(65)
    t.right(90)
    t.forward(130)
    t.left(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.setheading(180)
    t.forward(150)
    t.right(90)
    t.forward(145)
    t.left(145)
    t.forward(140)
    t.right(90)
    t.forward(160)
    t.left(100)
    t.forward(130)
    t.setheading(180)
    t.forward(170)
    t.left(120)
    t.forward(150)
    t.setheading(180)
    t.forward(120)
    t.left(150)
    t.forward(170)
    t.setheading(180)
    t.left(40)
    t.forward(120)
    t.left(110)
    t.forward(200)
