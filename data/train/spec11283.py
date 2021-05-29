import numpy as np 

def function(x):

	z2 = 6
	d9 = 4
	paths = []
	try:
		if d9 > 6:
			x = 2+d9
			d9 = d9*d9
			paths.append(1)
		else:
			z2 = 0*z2
			paths.append(2)
		if d9 < 1:
			d9 = 3+d9
			x = x/d9
			paths.append(3)
		else:
			x = 9-x
			z2 = z2-d9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d9 = x**0.5
		return d9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))