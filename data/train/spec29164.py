import numpy as np 

def function(x):

	z7 = x
	i4 = x
	paths = []
	try:
		if i4 >= 4:
			x = 4/x
			paths.append(1)
		else:
			z7 = x-3
			paths.append(2)
		if z7 >= 2:
			i4 = 5+2
			z7 = 0/4
			z7 = 4-z7
			paths.append(3)
		else:
			i4 = 6*9
			paths.append(4)
		paths.append(5)
		assert z7 >= 0
		z7 = z7**0.5
		return z7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))