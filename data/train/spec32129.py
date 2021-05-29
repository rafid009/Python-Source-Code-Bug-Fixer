import numpy as np 

def function(x):

	c6 = x
	v8 = 4
	paths = []
	try:
		if c6 <= 0:
			c6 = c6-7
			paths.append(1)
		else:
			c6 = c6-5
			paths.append(2)
		if v8 >= 1:
			x = v8-x
			v8 = c6*5
			c6 = 6*8
			paths.append(3)
		else:
			v8 = 9/2
			c6 = c6/c6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c6 = x**0.5
		return c6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))