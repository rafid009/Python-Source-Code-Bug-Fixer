import numpy as np 

def function(x):

	z4 = 5
	k2 = x
	paths = []
	try:
		if z4 > 2:
			k2 = 3*k2
			z4 = z4/1
			paths.append(1)
		else:
			k2 = 0+k2
			paths.append(2)
		if k2 > 4:
			k2 = 5*7
			k2 = k2-z4
			z4 = z4-k2
			paths.append(3)
		else:
			k2 = k2-8
			k2 = k2/k2
			z4 = z4/2
			paths.append(4)
		paths.append(5)
		assert z4 >= 0
		z4 = z4**0.5
		return z4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))