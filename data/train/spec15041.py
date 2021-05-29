import numpy as np 

def function(x):

	z8 = 6
	s8 = 2
	paths = []
	try:
		if x <= 5:
			s8 = 2+3
			z8 = z8*z8
			paths.append(1)
		else:
			z8 = s8-z8
			paths.append(2)
		if z8 < 7:
			s8 = s8/7
			x = 1*s8
			paths.append(3)
		else:
			z8 = z8*5
			s8 = 6-8
			paths.append(4)
		paths.append(5)
		assert z8 >= 0
		z8 = z8**0.5
		return z8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))