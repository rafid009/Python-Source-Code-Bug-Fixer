import numpy as np 

def function(x):

	z9 = x
	s5 = 8
	paths = []
	try:
		if z9 > 2:
			x = x/x
			z9 = z9/3
			s5 = s5/6
			paths.append(1)
		else:
			z9 = 3*9
			paths.append(2)
		if x < 9:
			z9 = z9/3
			s5 = z9+s5
			paths.append(3)
		else:
			s5 = x-5
			s5 = z9+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z9 = x**0.5
		return z9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))