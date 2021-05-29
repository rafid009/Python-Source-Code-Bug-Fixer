import numpy as np 

def function(x):

	d1 = 8
	a8 = x
	paths = []
	try:
		if d1 >= 8:
			x = x*7
			paths.append(1)
		else:
			a8 = a8-2
			paths.append(2)
		if x >= 0:
			x = 1-x
			a8 = d1+3
			d1 = d1+2
			paths.append(3)
		else:
			d1 = d1*x
			d1 = 8*d1
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