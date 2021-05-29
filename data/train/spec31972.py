import numpy as np 

def function(x):

	d5 = 1
	c8 = x
	paths = []
	try:
		if x <= 3:
			c8 = 8+2
			d5 = x+1
			paths.append(1)
		else:
			d5 = x+d5
			paths.append(2)
		if c8 >= 4:
			x = 7-x
			x = 4+x
			c8 = c8-0
			paths.append(3)
		else:
			x = 0*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c8 = x**0.5
		return c8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))