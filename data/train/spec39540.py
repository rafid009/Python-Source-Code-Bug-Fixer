import numpy as np 

def function(x):

	z6 = x
	s0 = x
	paths = []
	try:
		if z6 <= 4:
			z6 = z6/2
			x = 0/x
			x = 3+s0
			paths.append(1)
		else:
			z6 = 4-z6
			paths.append(2)
		if x < 6:
			s0 = x+4
			s0 = s0+s0
			paths.append(3)
		else:
			s0 = s0-2
			x = 6/2
			x = x-0
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