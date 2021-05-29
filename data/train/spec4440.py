import numpy as np 

def function(x):

	j5 = 8
	z6 = 0
	paths = []
	try:
		if x <= 7:
			z6 = 2-z6
			x = x+6
			paths.append(1)
		else:
			x = x-0
			z6 = z6+x
			x = 8+7
			paths.append(2)
		if x >= 4:
			x = x-x
			paths.append(3)
		else:
			z6 = 9-z6
			z6 = 0-z6
			paths.append(4)
		paths.append(5)
		assert z6 >= 0
		z6 = z6**0.5
		return z6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))