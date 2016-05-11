# 变量 & 表达式 & 语句

1. **值 & 变量**

   * When you type a large integer, you might be tempted to use commas between groups of three digits, as in 1,000,000. This is not a legal integer in Python, but it is legal:
     ~~~ bash
     >>> type(1,000,000)
     Traceback (most recent call last):
       File "<stdin>", line 1, in <module>
     TypeError: type() argument 1 must be string, not int
     >>> 1,000,000
     (1, 0, 0)
     ~~~
   
   Python interprets 1,000,000 as a commaseparated sequence of integers. This is a semantic error(语义错误)：the code runs without producing an error message, but it doesn’t do the “right” thing.

2. **变量**
   
   * 关于 **type()** 函数
     ~~~ python
     >>> type()
	  Traceback (most recent call last):
		 File "<stdin>", line 1, in <module>
	  TypeError: type() takes 1 or 3 arguments
     >>> type("1")
	  <type 'str'>
	  >>> type('2')
	  <type 'str'>
	  >>> type(1.0)
	  <type 'float'>
	  >>> type(1.000)
	  <type 'float'>
	  >>> type(0)
	  <type 'int'>
	  >>> type(T)
	  Traceback (most recent call last):
		 File "<stdin>", line 1, in <module>
	  NameError: name 'T' is not defined
	  >>> type(true)
	  Traceback (most recent call last):
		 File "<stdin>", line 1, in <module>
	  NameError: name 'true' is not defined
	  >>> type(t)
	  Traceback (most recent call last):
		 File "<stdin>", line 1, in <module>
	  NameError: name 't' is not defined
	  >>> type('true')
	  <type 'str'>
	  >>> type('')
	  <type 'str'>
	  >>> type(None)
	  <type 'NoneType'>
	  >>> type([])
	  <type 'list'>
	  >>> type(())
	  <type 'tuple'>
	  >>> type({})
	  <type 'dict'>
     ~~~

3. **变量名 & 关键字**
   
   * Variable can contain both letters and numbers, but they have to begin with a letter. The underscore character, _, can appear in a name.
   * keyword：
     <table>
        <tr>
           <td>with</td>
           <td>del</td>
           <td>yiele</td>
           <td>exec</td>
           <td>raise</td>
           <td>lambda</td>
           <td>assert</td>
           <td>global</td>
        </tr>
        <tr>
           <td>pass</td>
           <td>def</td>
           <td>except</td>
           <td>finally</td>
           <td>import</td>
           <td>continue</td>
           <td>or</td>
           <td>and</td>
        </tr>
        <tr>
           <td>from</td>
           <td>not</td>
           <td>if</td>
           <td>elif</td>
           <td>else</td>
        </tr>
        <tr>
           <td>in</td>
           <td>class</td>
           <td>for</td>
           <td>while</td>
           <td>break</td>
        </tr>
        <tr>
           <td>print</td>
           <td>return</td>
           <td>try</td>
           <td>is</td>
           <td>as</td>
        </tr>
     </table>
    
4. **操作符 & 操作数**
   
   * 除法：
     ~~~ bash
     >>> 60/59
     1
     >>> 59/60
     0
     ~~~
   
     In conventional arithmetic 59 divided by 60 is 0.98333, not 0.The reason for the discrepancy is that Python is performing **floor division**（除后向下圆整）.

5. **表达式 & 语句**
   
   * 这里没有什么需要注意的，唯一需要知道的就是在脚本中想要输出一个值不能写成表达式的样子，而是要写成 `print 表达式`。

6. **交互模式 & 脚本模式**

7. **运算次序**
   
   * rules of precedence（优先级法则）
     原来老外们是这么记的：

     **PEMDAS**：Parentheses + Exponents + Multiplication + Division + Addition + Subtraction

8. **字符串操作**
   
   * **+**：相当于 concatenation
   * *****：相当于 repetition

9. **注释**
   
   * python 将 # 开头到一行的末尾称为注释。
   * 还有一种类似多行注释的符号："""blah blah"""，这个被称为 docstring，会在第四章提到。

10. **调试**
   
    * SyntaxError
    * NameError
    * 虽然没有报错，但是结果不正确

11. **Glossary**

12. **Exercises**
  
    * The volume of a sphere with radius r is $$\frac{3}{4}πr^3$$. What is the volume of a sphere with radius 5? Hint: 392.7 is wrong!
      ~~~
      # Python 的整数除法是向下圆整的，所以写除法运算的时候记得写成浮点型。
      >>> import math
      >>> r = 5
      >>> (3.0 / 4) * math.pi * r ** 3
      294.5243112740431
      ~~~
 
    * Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?
      ~~~ bash
      >>> 24.95 * 60 * (100 - 40) * 0.01 + 1 * 3 + (60 - 1) * 0.75
      945.45
      ~~~

    * If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?
      ~~~ bash
      # 时
      >>> (((8 * 60 + 15) * 2 + (7 * 60 + 12) * 3) + 52 * 60 + 6 * 3600) / (60 * 60)
      7
      # 分
      >>> (((8 * 60 + 15) * 2 + (7 * 60 + 12) * 3) + 52 * 60 + 6 * 3600) % (60 * 60) / 60
      30
      # 秒
      >>> (((8 * 60 + 15) * 2 + (7 * 60 + 12) * 3) + 52 * 60 + 6 * 3600) % (60 * 60) % 60
      6
      ~~~

