import numpy as np 

def function(x):

	v1 = 2
	c3 = x
	paths = []
	try:
		if c3 >= 2:
			v1 = v1/v1
			v1 = x-8
			v1 = v1-7
			paths.append(1)
		else:
			c3 = 8*c3
			c3 = c3-5
			x = x/x
			paths.append(2)
		if x < 1:
			x = 6-x
			paths.append(3)
		else:
			x = x-v1
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