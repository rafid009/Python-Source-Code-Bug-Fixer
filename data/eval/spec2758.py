import numpy as np 

def function(x):

	x7 = 6
	z8 = x
	x = x
	paths = []
	try:
		if z8 <= 4:
			x = x+5
			x7 = 9+3
			paths.append(1)
		else:
			x = 8*x
			z8 = 3*z8
			z8 = x*z8
			paths.append(2)
		if x7 > 6:
			x7 = x7*7
			paths.append(3)
		else:
			x7 = 6/x7
			x7 = 9*x7
			paths.append(4)
		paths.append(5)
		assert z8 >= 0
		x7 = z8**0.5
		return x7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))