import numpy as np 

def function(x):

	u0 = 3
	c3 = x
	paths = []
	try:
		if u0 <= 3:
			u0 = u0*c3
			c3 = c3-c3
			paths.append(1)
		else:
			x = u0+x
			u0 = 8*u0
			x = u0+3
			paths.append(2)
		if c3 > 9:
			x = 7+4
			paths.append(3)
		else:
			c3 = u0+u0
			u0 = c3-0
			paths.append(4)
		paths.append(5)
		assert u0 >= 0
		c3 = u0**0.5
		return c3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))