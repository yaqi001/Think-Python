# Conditionals & Recursion

1. Modulus operator（模运算符）
   * For example, **x % 10** yields the right-most digit of x (in base 10). Similarly **x % 100** yields the last two digits.
   
2. 布尔表达式
   * 比较运算符，例：
     * x >= y   # x is greater than <font color='red'>or</font> equal to y
     * x <= y   # x is less than <font color='red'>or</font> equal to y

3. 逻辑运算符
   * and
   * or
   * not
   
   > **重要**：
   > Strictly speaking, the operands of the logical operators should be boolean expressions, but Python is not very strict. Any nonzero number is interpreted as “true.”
     ~~~ python
     -1.1 or True
     -1.1  # 这里为什么会返回 -1.1？因为 -1.1 is interpreted as "true"，所以不会再往下执行到 True，于是返回 -1.1
     >>> True or -1.1
	 True
	 >>> False or -1.1
	 -1.1
	 >>> -1.1 and True
	 True
     >>> True or 17
     True
     ~~~

4. 条件执行
   * 在不需要函数进行任何操作的时候，函数体中写 pass 即可。
     ~~~ bash
     >>> if x < 0:
	 ...    pass
	 ... 
     ~~~

5. 选择执行
   ~~~ python
   if x % 2 == 0:
	  print 'x is even'
   else:
      print 'x is odd'
   ~~~

6. Chained conditionals
   * **elif** is an abbreviation of “else if.”

7. Nested conditionals
   * 作者认为：即便缩进使得嵌套条件语句结构更加明显，但是读的效率却很低。于是作者想要避免使用嵌套语句，将其改为逻辑语句来执行。
     ~~~ python
     if x > 0:
        if x < 10:
           print 'x is less than zero and greater than ten.'
     ~~~
     
     上面的嵌套条件语句可以改写为如下语句：
     ~~~ python
     if x > 0 and x < 10:
        print 'x is less than zero and greater than ten.'
     ~~~

8. 递归
   * A function that calls itself is **recursive**; the process is called **recursion**. 

9. 递归函数的堆栈图
   * Every time a function gets called, Python creates a new function frame, which contains the function’s local variables and parameters. 
      * [递归函数执行过程](../images/out.ogv)
      * [global](../images/a.ogv)

10. **Infinite recursion**
    如果在一个程序中出现了无线递归，其实该程序并不会一直执行下去。而是当后台执行达到最大递归深度时，Python 就会报告错误：RuntimeError: maximum recursion depth exceeded。当这个错误出现时，你应该知道已经有 1000 个递归 frame 在 stack 中了。

11. **键盘输入**
    ~~~ bash
    >>> name = raw_input('What\'s your name?\n')
    What's your name?
    qiqi
    ~~~

12.
