import numpy as np 

def function(x):

	e8 = 4
	c4 = 0
	paths = []
	try:
		if e8 >= 1:
			e8 = e8/8
			e8 = 0*c4
			paths.append(1)
		else:
			c4 = 2+c4
			c4 = 3+c4
			c4 = 1+0
			paths.append(2)
		if e8 > 2:
			c4 = 5+3
			c4 = c4*1
			c4 = 7-c4
			paths.append(3)
		else:
			c4 = x-5
			e8 = e8+c4
			e8 = e8-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c4 = x**0.5
		return c4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))