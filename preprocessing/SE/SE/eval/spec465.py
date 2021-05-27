import numpy as np 

def function(x):

	d9 = 2
	c5 = x
	paths = []
	try:
		if c5 > 0:
			x = 2-7
			paths.append(1)
		else:
			d9 = d9*c5
			x = x+6
			paths.append(2)
		if x <= 2:
			d9 = c5/7
			paths.append(3)
		else:
			d9 = d9-6
			x = x*d9
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