# _*_ coding:utf-8 _*_

from space import *
from math import *

world = TurtleWorld()
bob = Turtle()
# 设置乌龟的初始地点
pu(bob)
fd(bob, 300)
rt(bob, 90)
fd(bob, 300)

# 设置让乌龟留下痕迹
pd(bob)
def circle(t, r):
   c = 2.0 * pi * r
   n = int(c / 3) + 1 
   l = c / n
   myploygon(t, n, l)

bob.delay = 0.01
circle(bob, 50)
