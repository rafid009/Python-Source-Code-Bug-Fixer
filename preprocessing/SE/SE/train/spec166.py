import numpy as np 

def function(x):

	s9 = x
	z8 = x
	paths = []
	try:
		if s9 < 0:
			s9 = s9-2
			x = x-7
			paths.append(1)
		else:
			s9 = z8+s9
			s9 = x/s9
			paths.append(2)
		if z8 <= 8:
			z8 = x+z8
			paths.append(3)
		else:
			s9 = z8+2
			x = x+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z8 = x**0.5
		return z8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))