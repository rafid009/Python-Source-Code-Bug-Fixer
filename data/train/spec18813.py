import numpy as np 

def function(x):

	z2 = x
	e7 = x
	paths = []
	try:
		if x > 7:
			x = 0-e7
			paths.append(1)
		else:
			z2 = 3-3
			x = x/e7
			paths.append(2)
		if z2 > 8:
			z2 = z2+9
			paths.append(3)
		else:
			x = z2+9
			x = z2/x
			z2 = z2-3
			paths.append(4)
		paths.append(5)
		assert e7 >= 0
		e7 = e7**0.5
		return e7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))