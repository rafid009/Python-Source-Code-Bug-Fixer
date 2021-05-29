import numpy as np 

def function(x):

	q0 = x
	c7 = 7
	x = x
	paths = []
	try:
		if c7 <= 9:
			c7 = 9-0
			c7 = c7-4
			paths.append(1)
		else:
			c7 = c7*3
			x = x*3
			paths.append(2)
		if q0 <= 3:
			q0 = 6-q0
			c7 = 1/3
			paths.append(3)
		else:
			c7 = q0+c7
			x = q0/c7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q0 = x**0.5
		return q0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))