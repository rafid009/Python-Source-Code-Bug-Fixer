import numpy as np 

def function(x):

	z5 = 6
	o6 = x
	paths = []
	try:
		if z5 < 3:
			o6 = 9+z5
			z5 = o6-z5
			paths.append(1)
		else:
			z5 = z5/2
			paths.append(2)
		if x >= 0:
			z5 = z5-7
			z5 = z5+o6
			paths.append(3)
		else:
			x = x+7
			x = 7+x
			z5 = x*z5
			paths.append(4)
		paths.append(5)
		assert z5 >= 0
		o6 = z5**0.5
		return o6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))