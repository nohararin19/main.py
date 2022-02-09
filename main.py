from module_Rick import Rick
from module_Morty import Morty
from module_space_shuttle import Spaceship
import turtle


r = Rick()
m = Morty()
s = Spaceship()

turtle.onkey(s.draw, 'Up')
turtle.listen()


turtle.done()
#dkc123