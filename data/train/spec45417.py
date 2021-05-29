import numpy as np 

def function(x):

	k6 = 3
	z6 = x
	paths = []
	try:
		if z6 < 6:
			x = 2+x
			z6 = x+z6
			paths.append(1)
		else:
			z6 = z6*k6
			k6 = 2*k6
			paths.append(2)
		if z6 >= 7:
			z6 = 5+7
			z6 = z6/2
			k6 = x-0
			paths.append(3)
		else:
			k6 = z6+k6
			k6 = 8/k6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z6 = x**0.5
		return z6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))