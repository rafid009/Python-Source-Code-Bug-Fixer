import numpy as np 

def function(x):

	y9 = x
	z2 = 5
	paths = []
	try:
		if x < 5:
			y9 = 1+9
			paths.append(1)
		else:
			z2 = 6/z2
			z2 = 6*7
			x = x-6
			paths.append(2)
		if x <= 3:
			z2 = z2-9
			x = 5/x
			x = x+4
			paths.append(3)
		else:
			x = 2*x
			z2 = 8*5
			paths.append(4)
		paths.append(5)
		assert z2 >= 0
		x = z2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))