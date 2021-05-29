import numpy as np 

def function(x):

	d2 = 3
	a3 = x
	paths = []
	try:
		if x < 1:
			a3 = a3*x
			paths.append(1)
		else:
			x = x-3
			a3 = a3+4
			a3 = 6*3
			paths.append(2)
		if d2 > 1:
			x = 8+x
			paths.append(3)
		else:
			d2 = 1/3
			a3 = 9+a3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d2 = x**0.5
		return d2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))