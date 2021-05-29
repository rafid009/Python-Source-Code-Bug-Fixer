import numpy as np 

def function(x):

	c7 = 1
	d2 = 9
	paths = []
	try:
		if x >= 8:
			x = 9*x
			paths.append(1)
		else:
			c7 = d2/c7
			paths.append(2)
		if c7 > 7:
			c7 = x+c7
			x = x-0
			d2 = d2+5
			paths.append(3)
		else:
			d2 = 2-d2
			d2 = x/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c7 = x**0.5
		return c7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))