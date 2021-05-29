import numpy as np 

def function(x):

	c6 = 5
	q8 = 5
	paths = []
	try:
		if x > 9:
			x = 6/x
			q8 = 8+q8
			paths.append(1)
		else:
			q8 = 8/q8
			paths.append(2)
		if c6 <= 2:
			q8 = x-q8
			x = 1+x
			x = x-x
			paths.append(3)
		else:
			x = q8/x
			q8 = q8/6
			c6 = q8-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q8 = x**0.5
		return q8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))