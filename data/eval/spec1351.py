import numpy as np 

def function(x):

	c5 = 9
	d0 = x
	paths = []
	try:
		if x >= 2:
			c5 = 0-5
			x = 1*x
			paths.append(1)
		else:
			d0 = d0/1
			c5 = 0-4
			paths.append(2)
		if c5 < 7:
			c5 = 5*3
			x = x*6
			d0 = d0/x
			paths.append(3)
		else:
			x = 9/x
			c5 = c5+4
			c5 = c5+1
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