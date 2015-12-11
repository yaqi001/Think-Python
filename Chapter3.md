# 方法

1. 方法调用
   
2. 类型转换函数
   
   1. **int()** 可以转换成任何类型的值，除了含有非数字的字符串。
      
      * int(float)

        > **注意**：int can convert floating-point values to integers, but it doesn’t round off; it <font color='red'>chops off</font> the fraction part:
        ~~~ bash
        >>> int(1.999)
        >>> 1
        >>> int(-5.23)
        -5
        >>>
        ~~~

      * int(bool)
        ~~~ bash
        >>> int(T)
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        NameError: name 'T' is not defined
        >>> int(True)
        1
        >>> int(False)
        0
        ~~~

      * int(string)
        ~~~ bash
        >>> int('12345')
        12345
        >>> int('12a)
          File "<stdin>", line 1
            int('12a)
                    ^
        SyntaxError: EOL while scanning string literal
        ~~~

   2. **float** can convert integers and strings to floating-point numbers.
      
      * float(int)
        ~~~ bash
        >>> float(111)
        111.0
        ~~~

      * float(string)
        ~~~ bash
        >>> float('111')
        111.0
        >>> float('111b')
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        ValueError: invalid literal for float(): 111b
        ~~~

      * float(bool)
        ~~~ bash
        >>> float(T)
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        NameError: name 'T' is not defined
        ~~~

   3. **str** can convert any kinds of type to string.
      
      * str(int)
        ~~~ bash
        >>> str(11)
        '11'
        ~~~

      * str(float)
        ~~~ bash
        >>> str(11.11)
        '11.11'
        ~~~

      * str(bool)
        ~~~ bash
        >>> str(T)
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        NameError: name 'T' is not defined
        >>> str(True)
        'True'
        ~~~

3. 数学函数

   * 对数
     ~~~ bash
     import math
     >>> math.log10(100)
     2.0
     >>> math.log(math.e)
     1.0
     ~~~
    
   * 三角函数
     ~~~ bash
     >>> degrees = 45
     >>> radians = degrees / 360.0 * 2 * math.pi
     >>> math.sin(radians)
     0.7071067811865475
     ~~~
 
     \\(radians=\frac{π}{4}\\)

     \\(\sin{\frac{π}{4}}=\frac{\sqrt{2}}{2}\\)
 
   * math.e
     ~~~ bash
     >>> math.exp(1)
     2.718281828459045
     >>> math.e
     2.718281828459045
     ~~~
    
4. Composition
    
   > **注意**：
   > the left side of an assignment statement has to be a variable name. Any other expression on the left side is a syntax error (we will see exceptions to this rule later).
     ~~~ bash 
     >>> hours = 1
     >>> minutes = hours * 60
     >>> hours * 60 = minutes
       File "<stdin>", line 1
     SyntaxError: can't assign to operator
     ~~~

5. 添加新的方法：
   
   * 关于方法名称需要注意的地方：
     1. 第一个字符不能是数字，其它位置可以是英语字母，数字或者一些标点符号。
     2. 不可以是关键字。
     3. 避免方法名称和变量名称相同。

   * **定义函数的同时会创建一个同名的变量**
     ~~~ bash
     >>> def first():
     ...    print 'hello world'
     ... 
     >>> first
     <function first at 0x7fe5331582a8>
     >>> type(first)
     <type 'function'>
     ~~~
     The value of first is a **function object**, which has type 'function'.
   
   * 一旦你定义了一个函数，你就可以在其它函数中使用该函数了。

6. 定义和使用：
    
   ~~~ python
   def print_lyrics():
      print "I am a lumberjack, and I'm okay."
      print "I sleep all night and I work all day."

   def repeat_lyrics():
      print_lyrics()
      print_lyrics()

   repeat_lyrics()
   ~~~

   * Exercise 3.1：Move the last line of this program to the top, so the function call appears before the definitions. Run the program and see what error message you get.
     ~~~ python
     repeat_lyrics()

     def print_lyrics():
        print "I am a lumberjack, and I'm okay."
        print "I sleep all night and I work all day."

     def repeat_lyrics():
        print_lyrics()
        print_lyrics()
     ~~~
  
     ~~~ bash
     # 运行结果
     [helen@zhangyingyun Python]$ python lyrics.py 
     Traceback (most recent call last):
       File "lyrics.py", line 1, in <module>
         repeat_lyrics()
     NameError: name 'repeat_lyrics' is not defined
     ~~~
   * Exercise 3.2：Move the function call back to the bottom and move the definition of print_lyrics after the definition of repeat_lyrics. What happens when you run this program?
     ~~~ python
     def repeat_lyrics():
        print_lyrics()
        print_lyrics()

     def print_lyrics():
        print "I am a lumberjack, and I'm okay."
        print "I sleep all night and I work all day."

     repeat_lyrics()  
     ~~~
     
     ~~~ bash
     # 运行结果
     I am a lumberjack, and I'm okay.
     I sleep all night and I work all day.
     I am a lumberjack, and I'm okay.
     I sleep all night and I work all day.
     ~~~

