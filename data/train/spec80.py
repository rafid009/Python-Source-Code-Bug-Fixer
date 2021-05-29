import numpy as np 

def function(x):

	z0 = 7
	d9 = 7
	paths = []
	try:
		if z0 <= 0:
			d9 = 1/6
			paths.append(1)
		else:
			d9 = 1+3
			d9 = 7-0
			paths.append(2)
		if x <= 9:
			z0 = z0*9
			x = 5/1
			x = x-z0
			paths.append(3)
		else:
			x = x*1
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