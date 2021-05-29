import numpy as np 

def function(x):

	q4 = 1
	z2 = 4
	paths = []
	try:
		if x >= 8:
			q4 = 8*9
			z2 = 2-z2
			paths.append(1)
		else:
			z2 = 4/z2
			paths.append(2)
		if x <= 7:
			z2 = z2-z2
			z2 = z2-4
			x = 9*x
			paths.append(3)
		else:
			q4 = 9*q4
			q4 = q4-q4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q4 = x**0.5
		return q4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))