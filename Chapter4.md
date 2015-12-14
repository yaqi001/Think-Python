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

3. 

























      
