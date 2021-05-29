import numpy as np 

def function(x):

	r7 = 2
	z4 = 9
	paths = []
	try:
		if z4 < 7:
			x = x-r7
			paths.append(1)
		else:
			z4 = 2+2
			paths.append(2)
		if z4 < 0:
			z4 = 3/4
			x = 8+8
			paths.append(3)
		else:
			r7 = 6-r7
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