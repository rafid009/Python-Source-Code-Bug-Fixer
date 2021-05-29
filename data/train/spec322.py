import numpy as np 

def function(x):

	d0 = 7
	z6 = x
	paths = []
	try:
		if x >= 1:
			x = z6*1
			paths.append(1)
		else:
			z6 = z6/8
			d0 = d0/2
			d0 = 7-d0
			paths.append(2)
		if x > 6:
			d0 = d0/2
			d0 = x/d0
			paths.append(3)
		else:
			x = 9+x
			z6 = 9+z6
			d0 = 5+d0
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