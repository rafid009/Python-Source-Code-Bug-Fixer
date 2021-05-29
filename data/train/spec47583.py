import numpy as np 

def function(x):

	c0 = x
	r4 = 6
	x = 4
	paths = []
	try:
		if r4 < 0:
			r4 = r4/2
			paths.append(1)
		else:
			x = x-9
			c0 = c0/r4
			paths.append(2)
		if r4 < 5:
			x = 1-x
			paths.append(3)
		else:
			r4 = 8-8
			r4 = 4-r4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r4 = x**0.5
		return r4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))