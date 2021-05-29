import numpy as np 

def function(x):

	z8 = x
	p8 = 7
	paths = []
	try:
		if p8 >= 9:
			x = x*8
			paths.append(1)
		else:
			z8 = x*z8
			z8 = 3-z8
			paths.append(2)
		if p8 <= 1:
			z8 = x/z8
			paths.append(3)
		else:
			x = x/x
			x = 0-x
			z8 = z8*p8
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