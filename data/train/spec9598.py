import numpy as np 

def function(x):

	j0 = 5
	c8 = x
	x = x
	paths = []
	try:
		if j0 <= 3:
			c8 = c8*4
			paths.append(1)
		else:
			c8 = 4-c8
			j0 = 5-9
			paths.append(2)
		if c8 < 8:
			c8 = c8/x
			j0 = j0*5
			paths.append(3)
		else:
			c8 = 3-c8
			x = 0+7
			paths.append(4)
		paths.append(5)
		assert j0 >= 0
		c8 = j0**0.5
		return c8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))