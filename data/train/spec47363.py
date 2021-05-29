import numpy as np 

def function(x):

	z0 = x
	d5 = 4
	paths = []
	try:
		if d5 <= 2:
			d5 = 7/2
			d5 = 1*d5
			paths.append(1)
		else:
			z0 = z0/1
			z0 = z0-6
			d5 = 7/4
			paths.append(2)
		if d5 <= 2:
			d5 = d5+d5
			z0 = 8/2
			z0 = z0+x
			paths.append(3)
		else:
			z0 = 5+2
			z0 = 7*x
			paths.append(4)
		paths.append(5)
		assert z0 >= 0
		d5 = z0**0.5
		return d5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))