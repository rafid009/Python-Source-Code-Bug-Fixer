import numpy as np 

def function(x):

	d9 = 7
	c2 = x
	paths = []
	try:
		if x < 9:
			x = 9+x
			d9 = 0+d9
			paths.append(1)
		else:
			x = 4*x
			d9 = 9-8
			d9 = d9-7
			paths.append(2)
		if c2 < 3:
			c2 = c2/2
			paths.append(3)
		else:
			x = x-5
			c2 = c2+d9
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