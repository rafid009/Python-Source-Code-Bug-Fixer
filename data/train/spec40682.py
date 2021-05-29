import numpy as np 

def function(x):

	z9 = 6
	z1 = 1
	x = x
	paths = []
	try:
		if z1 >= 1:
			z9 = x+z9
			x = 8/z9
			paths.append(1)
		else:
			z9 = 1+z9
			z1 = z1/6
			paths.append(2)
		if z9 <= 8:
			z9 = z9*9
			paths.append(3)
		else:
			z9 = z9+1
			z1 = z1+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z9 = x**0.5
		return z9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))