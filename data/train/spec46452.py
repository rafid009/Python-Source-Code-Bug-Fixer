import numpy as np 

def function(x):

	d0 = 9
	z9 = 0
	paths = []
	try:
		if d0 >= 1:
			z9 = z9-1
			z9 = z9+z9
			paths.append(1)
		else:
			x = x-9
			x = x/1
			x = d0*x
			paths.append(2)
		if x > 3:
			z9 = 2/z9
			z9 = z9+z9
			paths.append(3)
		else:
			d0 = d0+5
			x = x/z9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d0 = x**0.5
		return d0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))