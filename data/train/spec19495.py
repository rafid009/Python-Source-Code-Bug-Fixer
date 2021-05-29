import numpy as np 

def function(x):

	z1 = 0
	d0 = 7
	paths = []
	try:
		if x >= 8:
			z1 = z1*1
			d0 = x-d0
			paths.append(1)
		else:
			d0 = 1-d0
			x = x-7
			paths.append(2)
		if x < 0:
			x = x+d0
			paths.append(3)
		else:
			z1 = z1*7
			x = 7/x
			x = x+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z1 = x**0.5
		return z1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))