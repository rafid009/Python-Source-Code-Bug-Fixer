import numpy as np 

def function(x):

	a9 = 5
	z8 = 1
	paths = []
	try:
		if z8 > 7:
			a9 = a9/7
			x = 6+7
			z8 = z8+x
			paths.append(1)
		else:
			a9 = a9+2
			a9 = 2+a9
			paths.append(2)
		if z8 >= 9:
			z8 = 9+a9
			x = a9*1
			z8 = z8-2
			paths.append(3)
		else:
			z8 = z8*6
			a9 = a9*z8
			a9 = 5+x
			paths.append(4)
		paths.append(5)
		assert a9 >= 0
		z8 = a9**0.5
		return z8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))