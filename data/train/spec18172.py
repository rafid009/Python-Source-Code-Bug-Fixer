import numpy as np 

def function(x):

	e0 = x
	z6 = x
	paths = []
	try:
		if e0 < 4:
			x = 5+z6
			x = x-6
			paths.append(1)
		else:
			z6 = z6/x
			e0 = e0/3
			paths.append(2)
		if x >= 2:
			x = 3-8
			z6 = 2-z6
			e0 = e0-6
			paths.append(3)
		else:
			z6 = z6+1
			x = x-9
			x = x/e0
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