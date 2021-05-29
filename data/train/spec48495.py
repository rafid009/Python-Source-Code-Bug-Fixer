import numpy as np 

def function(x):

	c5 = x
	d7 = x
	paths = []
	try:
		if c5 < 3:
			x = 5*x
			paths.append(1)
		else:
			c5 = c5-d7
			paths.append(2)
		if x > 1:
			d7 = 1*4
			d7 = d7/8
			paths.append(3)
		else:
			c5 = c5/1
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