import numpy as np 

def function(x):

	c6 = 6
	a3 = 8
	paths = []
	try:
		if c6 > 6:
			x = 2/x
			x = x+x
			paths.append(1)
		else:
			x = x/3
			paths.append(2)
		if x > 1:
			a3 = 6+3
			c6 = a3-c6
			paths.append(3)
		else:
			c6 = x+6
			a3 = x+5
			a3 = 6/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a3 = x**0.5
		return a3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))