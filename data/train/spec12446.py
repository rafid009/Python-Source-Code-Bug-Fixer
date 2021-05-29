import numpy as np 

def function(x):

	z5 = 5
	n9 = x
	paths = []
	try:
		if z5 >= 2:
			x = x-z5
			paths.append(1)
		else:
			z5 = z5+8
			z5 = 8-z5
			z5 = z5-n9
			paths.append(2)
		if n9 < 2:
			x = 7+0
			x = x+n9
			paths.append(3)
		else:
			x = x*8
			z5 = z5/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n9 = x**0.5
		return n9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))