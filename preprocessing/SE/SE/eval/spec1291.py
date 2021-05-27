import numpy as np 

def function(x):

	d4 = 8
	e9 = 8
	paths = []
	try:
		if d4 < 0:
			d4 = e9+d4
			e9 = e9*3
			paths.append(1)
		else:
			e9 = e9+e9
			paths.append(2)
		if x <= 2:
			e9 = 9+e9
			d4 = 6-x
			paths.append(3)
		else:
			d4 = d4/d4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d4 = x**0.5
		return d4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))