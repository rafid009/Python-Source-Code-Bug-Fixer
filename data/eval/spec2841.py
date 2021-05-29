import numpy as np 

def function(x):

	z1 = 7
	a8 = 4
	paths = []
	try:
		if a8 <= 1:
			z1 = 5-z1
			a8 = a8-z1
			a8 = z1+7
			paths.append(1)
		else:
			a8 = z1/6
			z1 = z1/9
			paths.append(2)
		if x >= 8:
			z1 = 1/z1
			a8 = x*a8
			x = z1/5
			paths.append(3)
		else:
			a8 = 9*2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a8 = x**0.5
		return a8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))