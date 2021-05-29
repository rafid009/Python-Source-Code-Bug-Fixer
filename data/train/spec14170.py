import numpy as np 

def function(x):

	d2 = x
	z7 = 1
	paths = []
	try:
		if d2 <= 9:
			z7 = 8-3
			z7 = z7/7
			paths.append(1)
		else:
			d2 = d2/8
			paths.append(2)
		if z7 > 1:
			x = 1/x
			paths.append(3)
		else:
			d2 = 3-d2
			x = x/2
			d2 = d2*z7
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