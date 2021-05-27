import numpy as np 

def function(x):

	d2 = 3
	z6 = x
	paths = []
	try:
		if x > 5:
			d2 = 9+d2
			d2 = z6+d2
			paths.append(1)
		else:
			x = 5/z6
			x = x-6
			d2 = 1+d2
			paths.append(2)
		if z6 > 9:
			x = 1-x
			z6 = z6+d2
			z6 = 7+x
			paths.append(3)
		else:
			x = 6/x
			d2 = d2*d2
			x = 8+x
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