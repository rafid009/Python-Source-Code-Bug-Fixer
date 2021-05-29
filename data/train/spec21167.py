import numpy as np 

def function(x):

	c5 = x
	v0 = 2
	x = x
	paths = []
	try:
		if c5 >= 4:
			x = 4+9
			c5 = c5*6
			c5 = 2*c5
			paths.append(1)
		else:
			v0 = x-v0
			x = x+4
			c5 = 4+7
			paths.append(2)
		if c5 > 1:
			x = x*6
			v0 = v0-v0
			paths.append(3)
		else:
			v0 = v0+x
			x = x/v0
			v0 = c5*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c5 = x**0.5
		return c5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))