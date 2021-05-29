import numpy as np 

def function(x):

	e0 = x
	d4 = x
	paths = []
	try:
		if x >= 0:
			d4 = e0+d4
			paths.append(1)
		else:
			d4 = d4-6
			paths.append(2)
		if d4 >= 1:
			d4 = 3*d4
			d4 = e0-d4
			paths.append(3)
		else:
			e0 = 8-6
			d4 = d4*7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e0 = x**0.5
		return e0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))