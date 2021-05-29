import numpy as np 

def function(x):

	c7 = 8
	q3 = x
	paths = []
	try:
		if c7 <= 0:
			x = 5*q3
			x = x+q3
			paths.append(1)
		else:
			q3 = 6-1
			c7 = c7+3
			paths.append(2)
		if q3 >= 7:
			q3 = 5+4
			paths.append(3)
		else:
			q3 = q3+x
			c7 = 7/c7
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