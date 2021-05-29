import numpy as np 

def function(x):

	q6 = 7
	c6 = 0
	paths = []
	try:
		if x <= 5:
			q6 = 5/x
			paths.append(1)
		else:
			q6 = x+8
			paths.append(2)
		if q6 > 5:
			c6 = 9+0
			q6 = 7/q6
			paths.append(3)
		else:
			c6 = c6/7
			q6 = q6-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c6 = x**0.5
		return c6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))