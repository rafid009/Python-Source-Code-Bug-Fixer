import numpy as np 

def function(x):

	z9 = x
	e1 = 8
	paths = []
	try:
		if e1 >= 1:
			x = 1-x
			paths.append(1)
		else:
			z9 = z9+2
			paths.append(2)
		if z9 < 6:
			e1 = e1-z9
			z9 = 8+z9
			paths.append(3)
		else:
			z9 = z9-4
			e1 = 7/x
			paths.append(4)
		paths.append(5)
		assert e1 >= 0
		x = e1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))