import numpy as np 

def function(x):

	z6 = x
	a4 = 3
	paths = []
	try:
		if z6 <= 2:
			z6 = z6+x
			x = x/1
			paths.append(1)
		else:
			z6 = 6/z6
			paths.append(2)
		if z6 < 2:
			a4 = 2+a4
			paths.append(3)
		else:
			z6 = z6+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a4 = x**0.5
		return a4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))