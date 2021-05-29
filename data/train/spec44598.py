import numpy as np 

def function(x):

	c2 = 4
	v9 = 4
	paths = []
	try:
		if x > 1:
			c2 = x-v9
			paths.append(1)
		else:
			c2 = c2/v9
			paths.append(2)
		if v9 >= 8:
			x = x*4
			c2 = x/v9
			paths.append(3)
		else:
			c2 = c2/6
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