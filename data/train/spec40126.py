import numpy as np 

def function(x):

	q9 = 3
	z1 = x
	x = 7
	paths = []
	try:
		if x >= 8:
			z1 = 0/z1
			paths.append(1)
		else:
			x = 4-1
			paths.append(2)
		if z1 >= 4:
			q9 = z1-7
			z1 = 7/z1
			x = x-0
			paths.append(3)
		else:
			z1 = q9-z1
			paths.append(4)
		paths.append(5)
		assert q9 >= 0
		z1 = q9**0.5
		return z1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))