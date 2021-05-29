import numpy as np 

def function(x):

	o9 = 0
	z0 = x
	paths = []
	try:
		if z0 <= 6:
			x = 1/z0
			z0 = 0-0
			paths.append(1)
		else:
			x = 8*1
			paths.append(2)
		if x < 9:
			x = x-9
			paths.append(3)
		else:
			o9 = o9+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o9 = x**0.5
		return o9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))