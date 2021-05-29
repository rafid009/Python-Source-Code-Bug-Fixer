import numpy as np 

def function(x):

	z8 = 9
	y6 = 6
	paths = []
	try:
		if y6 > 5:
			z8 = z8-6
			z8 = z8+z8
			x = x+7
			paths.append(1)
		else:
			y6 = y6-2
			z8 = 6*z8
			paths.append(2)
		if x < 3:
			z8 = z8-8
			paths.append(3)
		else:
			x = 7/9
			paths.append(4)
		paths.append(5)
		assert z8 >= 0
		z8 = z8**0.5
		return z8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))