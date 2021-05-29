import numpy as np 

def function(x):

	c7 = 8
	q2 = 7
	paths = []
	try:
		if q2 <= 5:
			c7 = 1*5
			x = c7-c7
			c7 = c7*c7
			paths.append(1)
		else:
			x = c7-x
			paths.append(2)
		if q2 <= 4:
			c7 = 0+x
			x = c7-9
			paths.append(3)
		else:
			q2 = q2*c7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c7 = x**0.5
		return c7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))