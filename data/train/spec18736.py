import numpy as np 

def function(x):

	z2 = x
	s7 = 2
	paths = []
	try:
		if x < 3:
			x = s7*5
			x = 8+4
			paths.append(1)
		else:
			z2 = x*x
			z2 = x+z2
			paths.append(2)
		if x < 1:
			z2 = 5*z2
			paths.append(3)
		else:
			s7 = 1-2
			s7 = s7+s7
			paths.append(4)
		paths.append(5)
		assert z2 >= 0
		z2 = z2**0.5
		return z2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))