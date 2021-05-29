import numpy as np 

def function(x):

	c3 = x
	d8 = 1
	paths = []
	try:
		if d8 >= 9:
			d8 = 5-d8
			d8 = 2*d8
			paths.append(1)
		else:
			d8 = d8*9
			paths.append(2)
		if c3 < 2:
			c3 = c3*4
			d8 = c3+d8
			d8 = 6/6
			paths.append(3)
		else:
			x = 3*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d8 = x**0.5
		return d8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))