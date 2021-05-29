import numpy as np 

def function(x):

	c7 = x
	b8 = x
	paths = []
	try:
		if x >= 6:
			c7 = 7-c7
			c7 = c7/4
			c7 = b8+c7
			paths.append(1)
		else:
			b8 = 9-2
			paths.append(2)
		if x > 3:
			c7 = b8*c7
			paths.append(3)
		else:
			x = x+8
			b8 = 6-5
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