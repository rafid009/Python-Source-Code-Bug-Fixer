import numpy as np 

def function(x):

	z1 = 3
	s8 = x
	paths = []
	try:
		if s8 < 2:
			x = x+x
			paths.append(1)
		else:
			z1 = 4-z1
			s8 = s8+s8
			paths.append(2)
		if x > 3:
			s8 = s8-1
			s8 = s8*0
			s8 = s8-3
			paths.append(3)
		else:
			x = 2*x
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