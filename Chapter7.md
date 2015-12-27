# Iteration

2. One of the most common forms of multiple assignment is an **update**, where the new value of the variable depends on the old.
   * If you try to update a variable that doesn’t exist, you get an error, because **Python evaluates the right side before it assigns a value** to x:
     >>>  x = x + 1
	 Traceback (most recent call last):
	   File "<stdin>", line 1, in <module>
	 NameError: name 'x' is not defined

   
