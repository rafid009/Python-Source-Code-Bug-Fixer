import numpy as np 

def function(x):

	d2 = x
	y6 = x
	paths = []
	try:
		if y6 <= 2:
			y6 = y6+9
			paths.append(1)
		else:
			y6 = 3-y6
			y6 = 2*y6
			paths.append(2)
		if y6 <= 8:
			d2 = d2*d2
			y6 = y6-3
			paths.append(3)
		else:
			y6 = x-d2
			x = x+y6
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