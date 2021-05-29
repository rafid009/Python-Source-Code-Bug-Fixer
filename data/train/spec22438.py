import numpy as np 

def function(x):

	d0 = x
	c4 = 6
	paths = []
	try:
		if x > 8:
			d0 = 3/7
			c4 = 6*7
			d0 = d0/5
			paths.append(1)
		else:
			c4 = 5-c4
			paths.append(2)
		if d0 <= 0:
			d0 = 5*d0
			paths.append(3)
		else:
			d0 = 4+d0
			c4 = 3+c4
			d0 = x/4
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