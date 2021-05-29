import numpy as np 

def function(x):

	z5 = 1
	z1 = x
	paths = []
	try:
		if z5 <= 1:
			x = x-2
			paths.append(1)
		else:
			z5 = z5/x
			paths.append(2)
		if z5 >= 5:
			z1 = z1+1
			z5 = z5*1
			z5 = 4+6
			paths.append(3)
		else:
			z1 = 4+x
			z5 = z5-2
			paths.append(4)
		paths.append(5)
		assert z5 >= 0
		z5 = z5**0.5
		return z5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))