import numpy as np 

def function(x):

	q5 = 7
	z5 = 0
	paths = []
	try:
		if x >= 8:
			x = 4/x
			paths.append(1)
		else:
			q5 = 9-1
			paths.append(2)
		if z5 >= 4:
			x = z5/z5
			z5 = 6+z5
			q5 = 1*6
			paths.append(3)
		else:
			x = 9*x
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