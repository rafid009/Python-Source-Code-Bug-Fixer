import numpy as np 

def function(x):

	h6 = x
	z4 = 3
	paths = []
	try:
		if x > 8:
			x = 5-z4
			paths.append(1)
		else:
			z4 = z4*x
			x = x*0
			x = h6/5
			paths.append(2)
		if x > 4:
			x = 0-x
			z4 = 9+8
			paths.append(3)
		else:
			x = 5+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z4 = x**0.5
		return z4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))