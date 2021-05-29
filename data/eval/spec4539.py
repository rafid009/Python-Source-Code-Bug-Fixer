import numpy as np 

def function(x):

	z8 = 2
	s4 = x
	paths = []
	try:
		if s4 <= 6:
			x = x+5
			paths.append(1)
		else:
			z8 = z8+7
			paths.append(2)
		if s4 <= 1:
			s4 = 0+9
			z8 = s4-z8
			z8 = 6+x
			paths.append(3)
		else:
			s4 = z8/s4
			z8 = s4*z8
			s4 = 1*z8
			paths.append(4)
		paths.append(5)
		assert z8 >= 0
		x = z8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))