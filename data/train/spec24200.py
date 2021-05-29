import numpy as np 

def function(x):

	c6 = x
	r7 = x
	x = x
	paths = []
	try:
		if x < 0:
			c6 = 3-c6
			paths.append(1)
		else:
			r7 = r7+c6
			x = r7+7
			paths.append(2)
		if c6 < 1:
			x = x/c6
			c6 = c6*7
			paths.append(3)
		else:
			r7 = r7/r7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r7 = x**0.5
		return r7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))