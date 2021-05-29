import numpy as np 

def function(x):

	z9 = 6
	d0 = x
	x = 7
	paths = []
	try:
		if z9 > 5:
			z9 = d0*6
			d0 = 7/d0
			paths.append(1)
		else:
			d0 = 6/d0
			paths.append(2)
		if z9 > 8:
			z9 = 0-4
			d0 = d0+0
			d0 = 8-z9
			paths.append(3)
		else:
			x = 6-d0
			paths.append(4)
		paths.append(5)
		assert d0 >= 0
		d0 = d0**0.5
		return d0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))