import numpy as np 

def function(x):

	z6 = x
	a5 = 0
	paths = []
	try:
		if a5 <= 3:
			z6 = z6*7
			z6 = 8*a5
			paths.append(1)
		else:
			z6 = 7-z6
			x = 8/9
			z6 = a5/5
			paths.append(2)
		if a5 > 7:
			z6 = 1+3
			a5 = 0+a5
			z6 = x-x
			paths.append(3)
		else:
			x = x-4
			a5 = a5+2
			a5 = a5*z6
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