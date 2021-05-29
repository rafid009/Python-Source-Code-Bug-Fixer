import numpy as np 

def function(x):

	x5 = 1
	z2 = x
	paths = []
	try:
		if x5 >= 5:
			x = x-1
			z2 = z2/x5
			paths.append(1)
		else:
			x = x/x
			paths.append(2)
		if x <= 6:
			x5 = 4*z2
			paths.append(3)
		else:
			z2 = z2/x
			x5 = x5-6
			x = x5+x
			paths.append(4)
		paths.append(5)
		assert x5 >= 0
		z2 = x5**0.5
		return z2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))