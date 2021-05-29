import numpy as np 

def function(x):

	s4 = 6
	z4 = 9
	paths = []
	try:
		if s4 >= 7:
			z4 = z4/z4
			z4 = s4*9
			s4 = 4*s4
			paths.append(1)
		else:
			z4 = 0-z4
			paths.append(2)
		if x >= 2:
			s4 = s4+6
			paths.append(3)
		else:
			z4 = z4*9
			x = x+9
			paths.append(4)
		paths.append(5)
		assert z4 >= 0
		x = z4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))