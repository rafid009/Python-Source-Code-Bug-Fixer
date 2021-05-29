import numpy as np 

def function(x):

	z6 = x
	a5 = x
	paths = []
	try:
		if a5 > 8:
			a5 = a5*7
			z6 = 3/z6
			z6 = z6+x
			paths.append(1)
		else:
			a5 = a5*a5
			x = z6*2
			x = 0-1
			paths.append(2)
		if x > 8:
			a5 = a5*4
			z6 = 6*5
			paths.append(3)
		else:
			a5 = a5/a5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a5 = x**0.5
		return a5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))