import numpy as np 

def function(x):

	z8 = x
	i2 = x
	paths = []
	try:
		if x < 9:
			x = 2+0
			z8 = 0/3
			paths.append(1)
		else:
			z8 = z8-2
			paths.append(2)
		if x > 7:
			x = 9-x
			paths.append(3)
		else:
			z8 = 5+z8
			i2 = i2*5
			x = 7*z8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))