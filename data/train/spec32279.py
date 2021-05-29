import numpy as np 

def function(x):

	z0 = x
	s4 = x
	paths = []
	try:
		if z0 > 0:
			s4 = 2*s4
			paths.append(1)
		else:
			z0 = z0+7
			x = x+x
			s4 = 0+s4
			paths.append(2)
		if s4 <= 1:
			z0 = z0/8
			paths.append(3)
		else:
			x = x/4
			s4 = 7*s4
			s4 = s4+x
			paths.append(4)
		paths.append(5)
		assert s4 >= 0
		x = s4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))