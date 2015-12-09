# 方法

1. 方法调用
   

2. 类型转换函数
   
   1. **int** can convert floating-point values to integers, but it doesn't round off, it chops off the fraction part.
   ~~~ bash
   >>> int(1.999)
   >>> 1
   >>> int(-5.23)
   -5
   >>>
   ~~~
  
   2. **float** can convert integers and strings to floating-point numbers.

   3. **string** can convert any kinds of type to string.

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

   
