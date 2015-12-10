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

   ~~~ bash
   import math

   a = math.log10(100)
   b = math.log(math.e)
   print a
   print b
   ~~~
  
   输出结果：
   ~~~ bash
   2.0
   1.0
   ~~~

   
