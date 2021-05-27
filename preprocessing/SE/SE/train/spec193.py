import numpy as np 

def function(x):

	h2 = 7
	z2 = x
	paths = []
	try:
		if z2 > 0:
			z2 = z2*6
			paths.append(1)
		else:
			x = 6/7
			x = 8/4
			paths.append(2)
		if z2 > 9:
			x = 0*2
			paths.append(3)
		else:
			x = 9+h2
			paths.append(4)
		paths.append(5)
		assert z2 >= 0
		h2 = z2**0.5
		return h2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))