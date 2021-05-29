import numpy as np 

def function(x):

	s4 = x
	z5 = 2
	x = x
	paths = []
	try:
		if z5 < 5:
			x = x-6
			paths.append(1)
		else:
			s4 = 1/2
			s4 = s4*3
			z5 = x-z5
			paths.append(2)
		if z5 < 1:
			x = s4-s4
			paths.append(3)
		else:
			x = x/7
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