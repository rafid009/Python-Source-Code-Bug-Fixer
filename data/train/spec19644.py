import numpy as np 

def function(x):

	q7 = 5
	c0 = 3
	paths = []
	try:
		if c0 >= 6:
			c0 = c0+5
			paths.append(1)
		else:
			c0 = 4+7
			paths.append(2)
		if c0 >= 6:
			x = x-6
			c0 = 1-c0
			paths.append(3)
		else:
			c0 = 6*c0
			x = x-7
			q7 = q7+4
			paths.append(4)
		paths.append(5)
		assert c0 >= 0
		q7 = c0**0.5
		return q7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))