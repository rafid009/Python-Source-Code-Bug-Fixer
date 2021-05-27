import numpy as np 

def function(x):

	a9 = x
	c5 = 6
	paths = []
	try:
		if c5 < 2:
			x = x-4
			x = a9+1
			x = 7-c5
			paths.append(1)
		else:
			a9 = a9-4
			c5 = c5/7
			paths.append(2)
		if x > 9:
			a9 = a9+9
			paths.append(3)
		else:
			x = c5/x
			x = 2/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a9 = x**0.5
		return a9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))