import numpy as np 

def function(x):

	d9 = 3
	d1 = x
	paths = []
	try:
		if x <= 2:
			d9 = d9*5
			d9 = d9/x
			d9 = 2*d9
			paths.append(1)
		else:
			d1 = d1*6
			paths.append(2)
		if x <= 8:
			d9 = d9-6
			x = 7/x
			d9 = d9/4
			paths.append(3)
		else:
			d1 = d1*x
			d9 = 3+3
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