import numpy as np 

def function(x):

	r2 = 2
	c4 = x
	paths = []
	try:
		if c4 < 2:
			c4 = c4/1
			c4 = c4-x
			paths.append(1)
		else:
			x = x*4
			r2 = r2*x
			x = 5-x
			paths.append(2)
		if r2 <= 5:
			r2 = 1*r2
			x = 9/x
			r2 = r2/7
			paths.append(3)
		else:
			r2 = r2*c4
			x = 7/6
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