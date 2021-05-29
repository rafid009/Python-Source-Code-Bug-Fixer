import numpy as np 

def function(x):

	c0 = x
	v1 = x
	paths = []
	try:
		if x < 2:
			v1 = v1*7
			paths.append(1)
		else:
			x = 7-x
			paths.append(2)
		if v1 < 3:
			v1 = v1/5
			paths.append(3)
		else:
			x = x/7
			v1 = c0/1
			x = 5-c0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c0 = x**0.5
		return c0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))