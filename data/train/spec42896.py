import numpy as np 

def function(x):

	z0 = x
	a8 = x
	paths = []
	try:
		if z0 >= 2:
			a8 = a8-7
			z0 = x*4
			paths.append(1)
		else:
			z0 = a8*3
			x = 8*x
			a8 = a8+z0
			paths.append(2)
		if z0 <= 5:
			a8 = z0/8
			x = x*2
			a8 = 3-a8
			paths.append(3)
		else:
			z0 = 3/x
			x = z0+x
			paths.append(4)
		paths.append(5)
		assert z0 >= 0
		a8 = z0**0.5
		return a8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))