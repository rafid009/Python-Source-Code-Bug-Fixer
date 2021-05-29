import numpy as np 

def function(x):

	k6 = 0
	z0 = x
	paths = []
	try:
		if z0 >= 8:
			k6 = 3-k6
			x = x/5
			paths.append(1)
		else:
			z0 = z0*3
			k6 = k6*3
			k6 = 3/x
			paths.append(2)
		if k6 > 7:
			z0 = 4+x
			z0 = z0/5
			x = 8/x
			paths.append(3)
		else:
			x = k6+z0
			paths.append(4)
		paths.append(5)
		assert z0 >= 0
		k6 = z0**0.5
		return k6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))