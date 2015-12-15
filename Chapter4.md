# Case study: interface design

1. TurtleWorld
    
   * A **package** is a collection of modules.

   * If Swampy is installed as a package on your system, you can import *TurtleWorld* like follow:
     ~~~ python
     from swampy.TurtleWorld import *
     ~~~ 
  
   * If you downloaded the Swampy modules but did not install them as a package, you can either work in the directory that contains the Swampy files, or add that directory to Python’s search path. Then you can import *TurtleWorld* like follow:
     ~~~ python
     from TurtleWorld import *
     ~~~

     > **将外部模块添加到 python 搜索目录中的方法**：
     > 1. 在 python 的交互模式下执行： 
          ~~~ bash
          >>> import sys
          >>> sys.path
          ['', '/usr/lib/python2.7/site-packages/SimpleGUICS2Pygame-01.09.00-py2.7.egg', '/usr/lib64/python27.zip', '/usr/lib64/python2.7', '/usr/lib64/python2.7/plat-linux2', '/usr/lib64/python2.7/lib-tk', '/usr/lib64/python2.7/lib-old', '/usr/lib64/python2.7/lib-dynload', '/usr/lib64/python2.7/site-packages', '/usr/lib64/python2.7/site-packages/Numeric', '/home/helen/workspace/Del_Tool/python/swampy-2.1.7/build/lib/swampy', '/usr/lib64/python2.7/site-packages/gtk-2.0', '/usr/lib64/python2.7/site-packages/wx-2.8-gtk2-unicode', '/usr/lib/python2.7/site-packages']
          ~~~
     > 2. 在 */usr/lib64/python2.7/site-packages* 目录中添加一个以 **.pth** 结尾的文件，在文件中写入外部模块所在的路径，保存，就大功告成啦！

   * **画出正方形**
     ~~~ python
     # _*_ coding: utf-8 _*_

     from TurtleWorld import *

     world = TurtleWorld()
     bob = Turtle()
     # 设置乌龟的初始地点
     pu(bob)
     fd(bob, 300)
     rt(bob, 90)
     fd(bob, 300)

     # 设置让乌龟留下痕迹
     pd(bob)
     def myploygon(staff, n, l):
        """
           staff 就是画出图形的小乌龟
           n 就是该图形的边数
           l 就是边的长度
        """
        i = 0
        a = 360 / n
        for i in range(n):
           fd(staff, l)
           lt(staff, a)
     myploygon(bob, 4, 10)
     wait_for_user()
     ~~~

2. **Simple repetition**

   指的就是上面用的 for 方法。

3. 练习画圆：
   ~~~ bash
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
      n = 100
      l = 2.0 * pi * r / n
      myploygon(t, n, l)
    
   circle(bob, 50)
   ~~~

4. **Encapsulation**（封装）

   * Wrapping a piece of code up in a function is called **encapsulation**.
   * Benefit0:It attaches a name to the code, which serves as a kind of documentation.
   * Benefit1: if you re-use the code, it is more concise to call a function twice than to copy and paste the body!

5. **Generalization**（泛化） 
   
   * Adding a parameter to a function is called **generalization**.
   * **keyword arguments**
     * If you have more than a few numeric arguments, it is easy to forget what they are, or what order they should be in. It is legal, and sometimes helpful, to include the names of the parameters in the argument list. 写上形式参数的名称，顺序就可以任意了。

       ~~~ bash
       myploygon(bob, n = 10, l = 50)
       ~~~
 
       或
       ~~~ bash
       myploygon(l = 50, staff = bob, n = 10)
       ~~~      

6. **Interface design**
   * The **interface** of a function is a summary of how it is used: 
     * what are the parameters?
     * what does the function do?
     * what is the return value?
   
   * An interface is **"clean"** if it is "as simple as possible, but not simpler."


12. Exercise
    
    * Exercise 4.2. 
      ~~~ python
      # _*_ coding:utf-8 _*_

      from TurtleWorld import *
      import math

      world = TurtleWorld()
      bob = Turtle()

      def arc(t, r, num):
         angle = 360.0 / num
         arc_length = 2 * math.pi * r * angle / 720
         n = int(arc_length / 3) + 1
         step_length = arc_length / n
         step_angle = float(angle) * 2.0 / n
         for f in range(num):
            for i in range(n):
               fd(t, step_length)
               lt(t, step_angle)
               #fd(t, step_length)

            lt(t, angle)

            for j in range(n):
               fd(t, step_length)
               lt(t, step_angle)

            lt(t, 180 - angle)

      bob.delay = 0.01
      # num 是叶子的数量
      arc(bob, r = 300, num = 6)
      wait_for_user()
      ~~~
    
      # 规律
      ~~~ python
      # _*_ coding:utf-8 _*_

      from TurtleWorld import *
      import math

      world = TurtleWorld()
      bob = Turtle()

      def arc(t, r, num):
         angle = 360.0 / num
	 arc_length = 2 * math.pi * r * (1 / 3.0)
	 n = int(arc_length / 3) + 1
	 step_length = arc_length / n
	 # step_angle = float(angle) * 2.0 / n
	 step_angle = 120.0 / n

	 for f in range(num):
	    for i in range(n):
	       fd(t, step_length)
	       lt(t, step_angle)
	       #fd(t, step_length)

               lt(t, 60)
 
               for j in range(n):
	          fd(t, step_length)
		  lt(t, step_angle)

	    lt(t, 67.5)

      bob.delay = 0.01
      # num 是叶子的数量arc(bob, r = 300, num = 12)
      arc(bob, r = 50, num = 48)
      wait_for_user()
      ~~~ 


















      
