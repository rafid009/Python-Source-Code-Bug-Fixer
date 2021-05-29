import numpy as np 

def function(x):

	y1 = 6
	d6 = x
	paths = []
	try:
		if y1 < 2:
			x = 3-x
			paths.append(1)
		else:
			d6 = d6/x
			paths.append(2)
		if y1 < 3:
			x = y1*8
			paths.append(3)
		else:
			d6 = y1/d6
			d6 = x-y1
			d6 = 9*d6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y1 = x**0.5
		return y1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))