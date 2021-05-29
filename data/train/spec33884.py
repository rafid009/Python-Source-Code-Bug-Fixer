import numpy as np 

def function(x):

	z2 = x
	e7 = 3
	paths = []
	try:
		if x >= 3:
			e7 = e7/z2
			paths.append(1)
		else:
			x = x-z2
			x = x+5
			z2 = z2+6
			paths.append(2)
		if z2 > 5:
			x = 1*e7
			e7 = e7-z2
			paths.append(3)
		else:
			z2 = e7-z2
			e7 = 8-e7
			x = 8+x
			paths.append(4)
		paths.append(5)
		assert e7 >= 0
		z2 = e7**0.5
		return z2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))