import numpy as np 

def function(x):

	c9 = x
	v3 = x
	paths = []
	try:
		if c9 < 3:
			c9 = c9*v3
			x = x/4
			v3 = c9-1
			paths.append(1)
		else:
			c9 = v3-1
			c9 = 0+c9
			paths.append(2)
		if v3 < 3:
			x = 0*v3
			paths.append(3)
		else:
			c9 = 6-c9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v3 = x**0.5
		return v3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))