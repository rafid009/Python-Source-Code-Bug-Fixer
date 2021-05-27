import numpy as np 

def function(x):

	y8 = x
	z5 = 3
	paths = []
	try:
		if y8 >= 5:
			z5 = z5+y8
			z5 = z5+z5
			z5 = z5+z5
			paths.append(1)
		else:
			z5 = z5/x
			x = x/5
			paths.append(2)
		if z5 < 9:
			y8 = x+y8
			y8 = x-9
			paths.append(3)
		else:
			x = 6/x
			paths.append(4)
		paths.append(5)
		assert y8 >= 0
		x = y8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))