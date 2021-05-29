import numpy as np 

def function(x):

	z1 = x
	a9 = x
	paths = []
	try:
		if x > 6:
			a9 = a9+9
			z1 = z1/z1
			paths.append(1)
		else:
			z1 = z1+a9
			z1 = z1+2
			paths.append(2)
		if z1 >= 3:
			z1 = 0/z1
			a9 = 7-9
			a9 = a9-x
			paths.append(3)
		else:
			x = 2-x
			x = 2*x
			paths.append(4)
		paths.append(5)
		assert a9 >= 0
		z1 = a9**0.5
		return z1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))