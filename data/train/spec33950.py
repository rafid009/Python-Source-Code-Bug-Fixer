import numpy as np 

def function(x):

	r9 = x
	c0 = 1
	paths = []
	try:
		if c0 > 5:
			c0 = r9-c0
			c0 = 7/x
			paths.append(1)
		else:
			x = 6*6
			x = c0*5
			r9 = r9+0
			paths.append(2)
		if r9 > 8:
			r9 = 5*c0
			c0 = 4-c0
			paths.append(3)
		else:
			r9 = 9*r9
			x = x*9
			c0 = 9-c0
			paths.append(4)
		paths.append(5)
		assert r9 >= 0
		c0 = r9**0.5
		return c0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))