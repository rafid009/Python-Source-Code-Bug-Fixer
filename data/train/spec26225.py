import numpy as np 

def function(x):

	q8 = 9
	z4 = 1
	paths = []
	try:
		if q8 >= 6:
			q8 = 5*q8
			z4 = z4/3
			paths.append(1)
		else:
			x = 7/x
			q8 = 9/q8
			q8 = q8/4
			paths.append(2)
		if z4 <= 6:
			z4 = 0/1
			q8 = 1+x
			paths.append(3)
		else:
			x = x/4
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