import numpy as np 

def function(x):

	c3 = 9
	q4 = 4
	paths = []
	try:
		if x >= 6:
			c3 = 4/c3
			x = 3+7
			x = 0*x
			paths.append(1)
		else:
			q4 = q4/3
			c3 = c3/6
			paths.append(2)
		if q4 < 1:
			q4 = 3-q4
			paths.append(3)
		else:
			x = q4-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q4 = x**0.5
		return q4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))