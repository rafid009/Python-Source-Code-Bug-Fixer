import numpy as np 

def function(x):

	z7 = 8
	e4 = 5
	paths = []
	try:
		if e4 >= 8:
			e4 = 7/e4
			z7 = 8*z7
			z7 = 5/e4
			paths.append(1)
		else:
			z7 = 3+0
			x = 9+x
			paths.append(2)
		if e4 < 7:
			e4 = e4-6
			z7 = x+z7
			x = x+z7
			paths.append(3)
		else:
			e4 = 2+e4
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