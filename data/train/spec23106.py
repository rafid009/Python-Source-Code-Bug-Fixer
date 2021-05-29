import numpy as np 

def function(x):

	i6 = x
	z8 = x
	x = 7
	paths = []
	try:
		if z8 < 3:
			z8 = z8-x
			z8 = z8+0
			paths.append(1)
		else:
			z8 = i6/6
			paths.append(2)
		if x <= 5:
			x = x+i6
			paths.append(3)
		else:
			i6 = z8-8
			z8 = 7*z8
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