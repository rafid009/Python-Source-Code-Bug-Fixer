import numpy as np 

def function(x):

	a5 = 1
	c3 = 0
	paths = []
	try:
		if a5 >= 5:
			c3 = c3-0
			x = 8-x
			paths.append(1)
		else:
			c3 = c3/1
			x = x-9
			paths.append(2)
		if x <= 5:
			c3 = c3+6
			c3 = 9-c3
			a5 = 9-1
			paths.append(3)
		else:
			x = 7/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a5 = x**0.5
		return a5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))