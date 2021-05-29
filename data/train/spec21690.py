import numpy as np 

def function(x):

	y2 = 1
	d9 = x
	paths = []
	try:
		if d9 >= 2:
			d9 = 8/d9
			paths.append(1)
		else:
			y2 = y2-5
			y2 = d9/y2
			paths.append(2)
		if d9 > 2:
			d9 = 1/d9
			y2 = 9+2
			paths.append(3)
		else:
			x = d9-7
			x = x-x
			x = 3+d9
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