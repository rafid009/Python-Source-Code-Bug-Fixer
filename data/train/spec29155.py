import numpy as np 

def function(x):

	q6 = 8
	c6 = 1
	paths = []
	try:
		if q6 < 1:
			c6 = c6*8
			c6 = c6*q6
			paths.append(1)
		else:
			q6 = q6+7
			paths.append(2)
		if c6 <= 2:
			x = 1-6
			q6 = c6-8
			paths.append(3)
		else:
			c6 = c6-q6
			q6 = 2+x
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