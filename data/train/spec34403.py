import numpy as np 

def function(x):

	v9 = x
	z0 = x
	paths = []
	try:
		if z0 > 9:
			x = x*2
			z0 = 0+z0
			z0 = v9+9
			paths.append(1)
		else:
			v9 = 4*v9
			v9 = v9*x
			z0 = 2+z0
			paths.append(2)
		if x >= 6:
			x = x/8
			paths.append(3)
		else:
			x = z0/x
			paths.append(4)
		paths.append(5)
		assert z0 >= 0
		v9 = z0**0.5
		return v9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))