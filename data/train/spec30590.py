import numpy as np 

def function(x):

	s2 = x
	z4 = 9
	paths = []
	try:
		if z4 <= 1:
			x = x+5
			z4 = 3-z4
			x = x/9
			paths.append(1)
		else:
			x = 6*x
			paths.append(2)
		if s2 <= 6:
			s2 = s2-3
			x = x-z4
			s2 = 9*x
			paths.append(3)
		else:
			s2 = s2+s2
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