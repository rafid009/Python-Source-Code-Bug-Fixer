import numpy as np 

def function(x):

	j7 = 4
	z6 = x
	paths = []
	try:
		if z6 < 8:
			z6 = 3-j7
			paths.append(1)
		else:
			z6 = 6-z6
			z6 = 8*z6
			paths.append(2)
		if z6 > 9:
			z6 = j7/1
			j7 = j7/j7
			paths.append(3)
		else:
			z6 = z6+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z6 = x**0.5
		return z6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))