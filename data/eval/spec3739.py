import numpy as np 

def function(x):

	u2 = 5
	c8 = 4
	paths = []
	try:
		if x < 1:
			u2 = 1/u2
			x = x+4
			x = x*6
			paths.append(1)
		else:
			x = x*3
			c8 = 5+9
			x = u2+x
			paths.append(2)
		if x > 5:
			c8 = 0+c8
			x = 6+x
			u2 = 2-u2
			paths.append(3)
		else:
			x = 6*u2
			u2 = 5*7
			x = 1-x
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