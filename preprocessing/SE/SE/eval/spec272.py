import numpy as np 

def function(x):

	c4 = 0
	q5 = 5
	paths = []
	try:
		if c4 > 7:
			q5 = q5+6
			paths.append(1)
		else:
			q5 = 6-q5
			q5 = 7-q5
			c4 = c4*c4
			paths.append(2)
		if q5 > 5:
			x = 6/x
			paths.append(3)
		else:
			q5 = 4-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))