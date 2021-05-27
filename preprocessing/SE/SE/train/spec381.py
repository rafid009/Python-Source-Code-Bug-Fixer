import numpy as np 

def function(x):

	v1 = 3
	c0 = x
	paths = []
	try:
		if v1 >= 4:
			c0 = 7-c0
			paths.append(1)
		else:
			c0 = c0-4
			paths.append(2)
		if c0 < 7:
			c0 = c0*6
			v1 = 9+0
			x = v1+x
			paths.append(3)
		else:
			x = 3/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v1 = x**0.5
		return v1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))