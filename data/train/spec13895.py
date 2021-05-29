import numpy as np 

def function(x):

	y5 = x
	z9 = x
	paths = []
	try:
		if x >= 2:
			x = 4+1
			z9 = x/z9
			z9 = 4*z9
			paths.append(1)
		else:
			z9 = z9/x
			paths.append(2)
		if z9 < 9:
			x = y5*6
			x = x+x
			z9 = 1*z9
			paths.append(3)
		else:
			x = z9*z9
			paths.append(4)
		paths.append(5)
		assert y5 >= 0
		z9 = y5**0.5
		return z9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))