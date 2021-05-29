import numpy as np 

def function(x):

	a1 = 5
	z1 = x
	x = 8
	paths = []
	try:
		if a1 >= 6:
			x = z1/x
			x = 0-0
			paths.append(1)
		else:
			z1 = z1-3
			paths.append(2)
		if a1 < 0:
			a1 = 3*a1
			paths.append(3)
		else:
			z1 = 9/z1
			a1 = 7*a1
			z1 = z1-0
			paths.append(4)
		paths.append(5)
		assert z1 >= 0
		a1 = z1**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))