import numpy as np 

def function(x):

	d1 = x
	c1 = 9
	paths = []
	try:
		if d1 < 1:
			c1 = c1/3
			x = 5/x
			paths.append(1)
		else:
			x = 8-x
			c1 = 3/c1
			d1 = 7*d1
			paths.append(2)
		if d1 <= 5:
			d1 = c1+2
			x = 5-x
			c1 = 8-3
			paths.append(3)
		else:
			x = 9-x
			x = x-6
			d1 = x+7
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