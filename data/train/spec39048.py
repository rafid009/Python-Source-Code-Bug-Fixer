import numpy as np 

def function(x):

	z4 = x
	b1 = 3
	paths = []
	try:
		if b1 > 2:
			b1 = 5-b1
			z4 = 9/z4
			paths.append(1)
		else:
			z4 = z4-9
			x = 3*x
			paths.append(2)
		if b1 >= 7:
			z4 = z4-z4
			b1 = 1*6
			paths.append(3)
		else:
			z4 = 7+z4
			z4 = 0/z4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))