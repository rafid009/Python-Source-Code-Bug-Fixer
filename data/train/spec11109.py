import numpy as np 

def function(x):

	s8 = x
	z6 = 4
	paths = []
	try:
		if z6 < 9:
			x = 9+z6
			paths.append(1)
		else:
			s8 = x*1
			z6 = 2/z6
			z6 = z6/z6
			paths.append(2)
		if s8 <= 2:
			x = x*4
			x = 0-x
			paths.append(3)
		else:
			x = 9/s8
			x = 9*0
			z6 = z6+x
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