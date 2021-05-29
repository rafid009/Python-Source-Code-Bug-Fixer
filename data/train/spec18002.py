import numpy as np 

def function(x):

	h6 = x
	z7 = x
	paths = []
	try:
		if z7 < 0:
			z7 = z7/7
			paths.append(1)
		else:
			x = 7*x
			paths.append(2)
		if x >= 5:
			z7 = 2-6
			x = 7-x
			paths.append(3)
		else:
			z7 = z7*z7
			paths.append(4)
		paths.append(5)
		assert z7 >= 0
		h6 = z7**0.5
		return h6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))