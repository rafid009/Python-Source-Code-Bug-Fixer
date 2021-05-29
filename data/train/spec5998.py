import numpy as np 

def function(x):

	c0 = x
	v5 = 9
	paths = []
	try:
		if c0 < 1:
			v5 = 8*6
			paths.append(1)
		else:
			x = 2/7
			v5 = x-v5
			paths.append(2)
		if c0 > 3:
			v5 = 1*9
			paths.append(3)
		else:
			c0 = c0*v5
			paths.append(4)
		paths.append(5)
		assert c0 >= 0
		c0 = c0**0.5
		return c0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))