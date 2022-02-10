from module_Rick import Rick
from module_Morty import Morty
from module_space_shuttle import Spaceship
import turtle


r = Rick()
m = Morty()
s = Spaceship()

turtle.listen()
turtle.onkeypress(s.up, 'Up')
turtle.onkeypress(s.down, 'Down')
turtle.onkeypress(s.left, 'Left')
turtle.onkeypress(s.right, 'Right')

turtle.done()
