import numpy as np 

def function(x):

	d7 = 1
	z0 = x
	paths = []
	try:
		if d7 < 3:
			x = x-0
			x = 5-6
			x = 4-x
			paths.append(1)
		else:
			z0 = 5/z0
			d7 = z0/8
			x = x+6
			paths.append(2)
		if z0 > 6:
			d7 = 0*d7
			x = 2*z0
			d7 = z0/6
			paths.append(3)
		else:
			x = 1-x
			z0 = z0/5
			paths.append(4)
		paths.append(5)
		assert z0 >= 0
		d7 = z0**0.5
		return d7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))