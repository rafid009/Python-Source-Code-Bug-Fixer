import numpy as np 

def function(x):

	q7 = 7
	c3 = 3
	paths = []
	try:
		if q7 >= 5:
			c3 = 3+x
			x = 7*0
			paths.append(1)
		else:
			c3 = 8-c3
			paths.append(2)
		if q7 < 3:
			x = x-c3
			q7 = 1*q7
			paths.append(3)
		else:
			c3 = c3/q7
			x = x-2
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