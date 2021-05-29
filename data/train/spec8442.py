import numpy as np 

def function(x):

	z1 = x
	z7 = 0
	paths = []
	try:
		if x >= 4:
			x = x-x
			paths.append(1)
		else:
			z7 = x*z7
			paths.append(2)
		if z7 >= 1:
			z7 = 2+z7
			z1 = z1/z1
			paths.append(3)
		else:
			z1 = z7+x
			paths.append(4)
		paths.append(5)
		assert z1 >= 0
		z1 = z1**0.5
		return z1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))