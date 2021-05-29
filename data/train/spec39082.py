import numpy as np 

def function(x):

	q7 = x
	c7 = 0
	paths = []
	try:
		if c7 <= 2:
			q7 = q7/q7
			paths.append(1)
		else:
			c7 = 2-c7
			x = 0*x
			x = x-6
			paths.append(2)
		if q7 >= 5:
			x = 1+5
			paths.append(3)
		else:
			q7 = 2*1
			q7 = q7-6
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