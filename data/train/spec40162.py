import numpy as np 

def function(x):

	z7 = 0
	q6 = x
	paths = []
	try:
		if q6 >= 7:
			z7 = 1-z7
			paths.append(1)
		else:
			x = z7*x
			paths.append(2)
		if z7 <= 2:
			z7 = z7*5
			z7 = z7-9
			paths.append(3)
		else:
			z7 = z7*z7
			q6 = 2/5
			paths.append(4)
		paths.append(5)
		assert z7 >= 0
		x = z7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))