# Fruitful functions

1. 返回值
   * In a fruitful function, it is a good idea to ensure that every possible path through the program hits a **return** statement.
     ~~~ python
     def absolute_value(x):
        if x < 0:
           return -x
        if x > 0:
           return x 

     print absolute_value(0)
     ~~~

     ~~~ bash
     # 返回结果
     [helen@zhangyingyun thinkPython]$ python return.py 
     None
     ~~~

2. Incremental development（增量式开发）

3. Composition
   * As you should expect by now, you can call one function from within another. This ability is called **composition**.

4. 布尔函数

5. 更多的递归

6. **Leap of faith**（一百八十度转变）


