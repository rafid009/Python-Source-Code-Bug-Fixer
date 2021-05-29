import numpy as np 

def function(x):

	z1 = 4
	f6 = x
	paths = []
	try:
		if x < 2:
			z1 = x+z1
			paths.append(1)
		else:
			z1 = z1+4
			f6 = f6/5
			f6 = 7/3
			paths.append(2)
		if f6 > 2:
			z1 = z1/6
			paths.append(3)
		else:
			z1 = 3/z1
			z1 = z1-z1
			f6 = 0+f6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z1 = x**0.5
		return z1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))