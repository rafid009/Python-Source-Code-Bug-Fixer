import numpy as np 

def function(x):

	z5 = x
	s8 = 1
	paths = []
	try:
		if z5 > 0:
			z5 = x/5
			s8 = 2/s8
			paths.append(1)
		else:
			x = x+0
			z5 = 8-6
			s8 = s8/1
			paths.append(2)
		if x < 4:
			z5 = z5-0
			z5 = 5+z5
			s8 = s8-z5
			paths.append(3)
		else:
			s8 = s8/x
			x = z5/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z5 = x**0.5
		return z5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))