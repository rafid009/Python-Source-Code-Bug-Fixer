import numpy as np 

def function(x):

	q9 = 0
	c6 = 2
	paths = []
	try:
		if c6 >= 9:
			x = q9*x
			x = 7/x
			c6 = q9*1
			paths.append(1)
		else:
			q9 = q9+3
			x = x+9
			paths.append(2)
		if c6 > 2:
			c6 = x*q9
			c6 = 7/c6
			paths.append(3)
		else:
			x = q9-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q9 = x**0.5
		return q9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))