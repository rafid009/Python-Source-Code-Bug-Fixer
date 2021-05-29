import numpy as np 

def function(x):

	c5 = 4
	q6 = 4
	paths = []
	try:
		if c5 >= 9:
			q6 = q6/q6
			q6 = 7*q6
			paths.append(1)
		else:
			x = 7/4
			x = x-c5
			q6 = q6*9
			paths.append(2)
		if x >= 4:
			q6 = q6+7
			c5 = x-2
			paths.append(3)
		else:
			c5 = 4+c5
			c5 = 9+x
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