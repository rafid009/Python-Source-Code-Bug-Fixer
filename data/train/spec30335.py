import numpy as np 

def function(x):

	n2 = 6
	z5 = 2
	paths = []
	try:
		if n2 <= 2:
			x = x+x
			paths.append(1)
		else:
			x = 2/x
			paths.append(2)
		if z5 <= 7:
			z5 = 0/z5
			paths.append(3)
		else:
			z5 = 9/9
			x = z5/z5
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