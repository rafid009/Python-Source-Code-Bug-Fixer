import numpy as np 

def function(x):

	e9 = 8
	z6 = 3
	paths = []
	try:
		if x >= 7:
			z6 = z6+6
			z6 = 4/z6
			paths.append(1)
		else:
			e9 = 5-5
			paths.append(2)
		if x <= 9:
			z6 = e9*2
			e9 = 9-e9
			paths.append(3)
		else:
			x = x/5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z6 = x**0.5
		return z6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))