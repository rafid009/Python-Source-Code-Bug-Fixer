import numpy as np 

def function(x):

	c3 = 6
	v8 = 8
	paths = []
	try:
		if v8 > 8:
			c3 = c3*c3
			x = v8/4
			v8 = v8-v8
			paths.append(1)
		else:
			c3 = c3-7
			c3 = c3*6
			c3 = 4+c3
			paths.append(2)
		if x >= 7:
			c3 = 6-2
			c3 = c3+v8
			paths.append(3)
		else:
			c3 = c3-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c3 = x**0.5
		return c3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))