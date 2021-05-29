import numpy as np 

def function(x):

	c6 = x
	d2 = 6
	paths = []
	try:
		if x >= 6:
			d2 = 2+2
			x = c6+x
			c6 = c6+5
			paths.append(1)
		else:
			x = c6+6
			x = 7+x
			c6 = d2/5
			paths.append(2)
		if c6 >= 5:
			x = c6-x
			x = 3-x
			paths.append(3)
		else:
			c6 = d2+x
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