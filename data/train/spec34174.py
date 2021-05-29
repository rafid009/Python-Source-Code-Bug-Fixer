import numpy as np 

def function(x):

	l4 = 8
	z6 = 8
	paths = []
	try:
		if z6 <= 9:
			l4 = x-5
			z6 = 1*4
			paths.append(1)
		else:
			l4 = 3*l4
			paths.append(2)
		if l4 < 8:
			z6 = 4/z6
			x = x-5
			paths.append(3)
		else:
			x = 0/x
			paths.append(4)
		paths.append(5)
		assert l4 >= 0
		z6 = l4**0.5
		return z6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))