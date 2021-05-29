import numpy as np 

def function(x):

	d2 = x
	c6 = x
	paths = []
	try:
		if d2 <= 6:
			x = x*x
			paths.append(1)
		else:
			c6 = c6+9
			paths.append(2)
		if x < 6:
			c6 = 4/c6
			paths.append(3)
		else:
			c6 = 2-c6
			x = d2*x
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