import numpy as np 

def function(x):

	r4 = 7
	c8 = x
	paths = []
	try:
		if c8 >= 1:
			c8 = 3*c8
			paths.append(1)
		else:
			x = x+1
			c8 = r4+c8
			paths.append(2)
		if c8 >= 1:
			r4 = 8/r4
			x = 5+x
			x = c8+6
			paths.append(3)
		else:
			r4 = 4+c8
			x = 5*x
			r4 = r4*8
			paths.append(4)
		paths.append(5)
		assert r4 >= 0
		c8 = r4**0.5
		return c8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))