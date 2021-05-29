import numpy as np 

def function(x):

	z6 = 5
	k5 = 5
	paths = []
	try:
		if z6 <= 0:
			z6 = x+6
			paths.append(1)
		else:
			z6 = z6/z6
			z6 = 4*5
			paths.append(2)
		if k5 >= 0:
			z6 = x+7
			x = 4/x
			paths.append(3)
		else:
			k5 = 9*k5
			x = x+4
			paths.append(4)
		paths.append(5)
		assert z6 >= 0
		x = z6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))