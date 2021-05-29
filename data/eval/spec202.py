import numpy as np 

def function(x):

	p8 = 2
	c6 = x
	x = 1
	paths = []
	try:
		if x <= 1:
			c6 = x-p8
			c6 = 7/c6
			p8 = p8/7
			paths.append(1)
		else:
			c6 = 0-4
			paths.append(2)
		if x <= 5:
			x = x-9
			c6 = c6/4
			paths.append(3)
		else:
			c6 = 6+2
			c6 = 0/c6
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