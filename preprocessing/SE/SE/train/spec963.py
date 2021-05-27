import numpy as np 

def function(x):

	y4 = x
	z6 = 8
	x = 5
	paths = []
	try:
		if z6 < 6:
			z6 = 0+z6
			paths.append(1)
		else:
			y4 = x*7
			x = z6*4
			z6 = z6-0
			paths.append(2)
		if y4 >= 5:
			x = x*7
			y4 = z6-y4
			x = 3/x
			paths.append(3)
		else:
			z6 = z6/3
			x = 4/x
			paths.append(4)
		paths.append(5)
		assert y4 >= 0
		z6 = y4**0.5
		return z6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))