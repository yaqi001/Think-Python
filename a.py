from TurtleWorld import *
from math import *
from ellipse import *

def drawEayun(t):
   # print E
   bk(t, 50)
   rt(t, 90)
   fd(t, 25)
   lt(t, 90)
   fd(t, 50)
   bk(t, 50)
   rt(t, 90)
   fd(t, 25)
   lt(t, 90) 
   fd(t, 50)
   
   # print a
   pu(t)
   fd(t, 25 / 2.0)
   pd(t)
   circle(t, 50 / 4.0)
 
   # print y
   pu(t)
   bk(t, 25)
   a = atan(1.0 / 2) * 360.0 / (2 * pi)
   lt(t, a)
   Yl = sqrt(25 ** 2 + 50 ** 2)
   pd(t)
   fd(t, Yl)
   pu(t)
   rt(t, 2 * a)
   fd(t, Yl)
   pd(t)
   bk(t, 2 * Yl)

   # print u
   rt(t, a)
   fd(t, 25)


world = TurtleWorld()
Bob = Turtle()
Bob.delay = 0.01
drawEayun(Bob)
wait_for_user()
