import numpy as np 

def function(x):

	z8 = x
	y5 = x
	paths = []
	try:
		if y5 < 0:
			y5 = y5/7
			y5 = y5/1
			y5 = 9+x
			paths.append(1)
		else:
			x = z8*x
			paths.append(2)
		if z8 < 8:
			z8 = 3-z8
			x = 3-x
			x = y5-7
			paths.append(3)
		else:
			y5 = 7/y5
			y5 = y5-x
			z8 = y5*z8
			paths.append(4)
		paths.append(5)
		assert z8 >= 0
		x = z8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))