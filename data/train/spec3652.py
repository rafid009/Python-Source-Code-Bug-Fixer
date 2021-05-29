import numpy as np 

def function(x):

	z9 = 6
	s4 = x
	paths = []
	try:
		if x <= 9:
			z9 = z9*6
			paths.append(1)
		else:
			z9 = z9-x
			paths.append(2)
		if x >= 1:
			z9 = s4-0
			paths.append(3)
		else:
			z9 = z9/z9
			s4 = s4/2
			z9 = s4*x
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