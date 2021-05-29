import numpy as np 

def function(x):

	k1 = 4
	z1 = x
	paths = []
	try:
		if z1 < 7:
			z1 = x*z1
			z1 = k1*4
			paths.append(1)
		else:
			k1 = k1-7
			k1 = k1-k1
			paths.append(2)
		if k1 > 5:
			x = 3/k1
			paths.append(3)
		else:
			z1 = z1-k1
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