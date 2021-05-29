import numpy as np 

def function(x):

	z0 = 9
	s0 = 3
	paths = []
	try:
		if z0 <= 7:
			s0 = s0-0
			paths.append(1)
		else:
			z0 = 8/x
			paths.append(2)
		if z0 > 7:
			z0 = s0/9
			paths.append(3)
		else:
			z0 = x-7
			s0 = 0+s0
			paths.append(4)
		paths.append(5)
		assert z0 >= 0
		x = z0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))