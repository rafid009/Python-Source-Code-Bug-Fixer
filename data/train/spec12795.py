import numpy as np 

def function(x):

	s2 = x
	z5 = 8
	paths = []
	try:
		if x < 9:
			x = x+z5
			paths.append(1)
		else:
			s2 = s2*0
			x = x*4
			x = x*6
			paths.append(2)
		if x >= 8:
			x = 5-4
			s2 = 4*s2
			z5 = 5-7
			paths.append(3)
		else:
			s2 = s2+s2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z5 = x**0.5
		return z5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))