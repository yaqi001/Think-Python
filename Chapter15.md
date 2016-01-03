# Classes & Objects

1. A user-defined type is also called a **class**.
   ~~~ python
   Class B(object):
      """define a class"""
   ~~~

   ~~~ bash
   >>> b = B()
   >>> B
   <class '__main__.B'>
   >>> b
   <__main__.B object at 0x7f4800001f90>
   >>> int
   <type 'int'>
   #---------------------------------------
   >>> type(int)
   <type 'type'>
   >>> type(B)
   <type 'type'>
   >>> type(b)
   <class '__main__.B'>
   ~~~

3. Rectangles
   * An object that is an attribute of another object is **embedded**.

	 ~~~ python
	 class A(object):
	    """A"""
	    aa = 'hello'
	    def set_aa(self, aa):
		   self.aa = aa
			
		def show(self):
		   print self.aa

	 a = A()
	 a.set_aa('halo')
	 a.aa = 'a'
	 a.age = 12
	 a.show()

	 class B(object):
	    """B"""
			
	 b = B()
	 b.corner = A() # A() 对象是 b 这个对象的属性。 
	 b.corner.aa = 'hello world'
	 b.corner.show()
		
	 b = 12
	 def C():
	    c = 12
	    print c
			
	 C()
	 ~~~

4. **Instances as result values**
   * 写法一：
     ~~~ python
     class Point(object):
	    def __init__(self, x, y):
	       self.x = x
		   self.y = y

	 class rectangle(object):
		def __init__(self, width, height, x, y):
		   self.width = width
		   self.height = height
		   self.x = x
		   self.y = y
		   self.corner = Point(self.x, self.y)

	 r = rectangle(10, 10, 1, 1)

	 def find_center(object):
        x = object.x + object.width / 2.0
		y = object.y + object.height / 2.0
		return Point(x, y)

	 print find_center(r).x, find_center(r).y
     ~~~

   * 写法二：
	 ~~~ python
	 class Point(object):
	    """Represents a point in 2-D space."""

	 def print_point(p):
	    print '(%g, %g)' % (p.x, p.y)


	 class Rectangle(object):
	    """Represents a rectangle.
 
        attributes: width, height, corner.
	    """

	 box = Rectangle()
	 box.width = 100.0
	 box.height = 200.0
	 box.corner = Point()
	 box.corner.x = 0.0
	 box.corner.y = 0.0

	 def find_center(rect):
	    p = Point()
	    p.x = rect.corner.x + rect.width / 2.0
	    p.y = rect.corner.y + rect.height / 2.0
	    return p

     center = find_center(box)
     print_point(center)
     ~~~
  
	 ~~~ bash
	 # 返回结果
 	 (50, 100)
     ~~~

6. **Coping**
   * This operation is called a **shallow copy** because it copies the object and any references it contains, but not the embedded objects.
   * Fortunately, the copy module contains a method named **deepcopy** that copies not only the object but also the objects it refers to, and the objects they refer to, and so on. You will not be surprised to learn that this operation is called a deep copy.

7. **Debugging**

   * If you are not sure whether an object has a particular attribute, you can use the built-in function **hasttr**: 
   * The first argument can be any object; the second argument is a string that contains the name of the attribute.
  
	 ~~~ bash
	 >>> hasattr('s', '__len__')
	 True
	 >>> hasattr('s', '__len_')
	 False
	 >>> hasattr('s', 'index')
	 True
	 >>> class A(object):
	 ...    def show(self):
	 ...       print self.x
	 ... 
	 >>> a = A()
	 >>> a.x = 1
	 >>> a.show()
	 1
	 >>> hasattr(a, 'show')
	 True
	 >>> hasattr(a, 'a')
	 False
	 >>> hasattr(a, 'x')
	 True
	 ~~~

8. 
   



















