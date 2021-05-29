import numpy as np 

def function(x):

	z6 = 4
	s8 = 0
	paths = []
	try:
		if z6 <= 6:
			s8 = s8/3
			paths.append(1)
		else:
			x = 0*x
			z6 = 1*x
			z6 = x*3
			paths.append(2)
		if s8 >= 9:
			x = x/8
			x = x+2
			paths.append(3)
		else:
			s8 = 1*s8
			z6 = z6-2
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