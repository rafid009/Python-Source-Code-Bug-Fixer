import numpy as np 

def function(x):

	v0 = x
	c1 = x
	paths = []
	try:
		if c1 < 4:
			c1 = c1*c1
			x = x+1
			paths.append(1)
		else:
			x = 1/v0
			v0 = v0+c1
			v0 = 8-1
			paths.append(2)
		if c1 < 4:
			c1 = c1-3
			x = x+7
			paths.append(3)
		else:
			v0 = v0*x
			paths.append(4)
		paths.append(5)
		assert v0 >= 0
		c1 = v0**0.5
		return c1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))