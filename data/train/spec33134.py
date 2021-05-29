import numpy as np 

def function(x):

	e0 = 5
	c0 = 4
	paths = []
	try:
		if e0 >= 9:
			x = x/9
			paths.append(1)
		else:
			e0 = e0/2
			c0 = 3+c0
			c0 = c0-8
			paths.append(2)
		if x <= 7:
			e0 = 0-e0
			paths.append(3)
		else:
			c0 = 3-7
			x = 8*4
			x = 0*1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c0 = x**0.5
		return c0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))