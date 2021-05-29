import numpy as np 

def function(x):

	z8 = 5
	q5 = x
	paths = []
	try:
		if q5 > 5:
			z8 = 4+7
			x = x-2
			paths.append(1)
		else:
			z8 = z8-5
			q5 = 3+q5
			paths.append(2)
		if z8 >= 4:
			q5 = 6/8
			paths.append(3)
		else:
			x = 9+x
			z8 = z8*q5
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