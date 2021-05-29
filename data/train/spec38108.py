import numpy as np 

def function(x):

	c4 = x
	x2 = 8
	paths = []
	try:
		if x < 0:
			x2 = 0-8
			x2 = x-x2
			c4 = c4+4
			paths.append(1)
		else:
			x = 0*4
			x2 = 5-x2
			paths.append(2)
		if x > 9:
			c4 = c4*2
			x2 = 9+x2
			paths.append(3)
		else:
			x2 = x2-4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x2 = x**0.5
		return x2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))