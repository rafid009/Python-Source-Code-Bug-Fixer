import numpy as np 

def function(x):

	d9 = 8
	c9 = 4
	paths = []
	try:
		if c9 < 3:
			x = x*3
			d9 = 4-7
			x = x+c9
			paths.append(1)
		else:
			c9 = d9-c9
			paths.append(2)
		if d9 < 6:
			d9 = d9/1
			paths.append(3)
		else:
			x = 8-x
			c9 = 4-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d9 = x**0.5
		return d9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))