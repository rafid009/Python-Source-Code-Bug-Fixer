import numpy as np 

def function(x):

	z5 = 6
	s7 = x
	paths = []
	try:
		if z5 >= 9:
			z5 = 3+7
			paths.append(1)
		else:
			z5 = s7/z5
			z5 = z5*2
			paths.append(2)
		if x <= 0:
			s7 = 9+s7
			x = s7+z5
			paths.append(3)
		else:
			x = x*0
			z5 = x-z5
			paths.append(4)
		paths.append(5)
		assert s7 >= 0
		x = s7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))