import numpy as np 

def function(x):

	z9 = 2
	y0 = x
	x = x
	paths = []
	try:
		if y0 < 2:
			x = z9+x
			paths.append(1)
		else:
			x = y0-6
			paths.append(2)
		if y0 >= 8:
			x = x-7
			paths.append(3)
		else:
			x = y0*x
			x = x*y0
			x = 7*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z9 = x**0.5
		return z9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))