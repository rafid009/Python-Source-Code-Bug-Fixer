import numpy as np 

def function(x):

	n2 = x
	z6 = 7
	paths = []
	try:
		if x >= 7:
			n2 = 9/x
			paths.append(1)
		else:
			z6 = z6/x
			z6 = x/8
			n2 = n2+5
			paths.append(2)
		if n2 < 4:
			z6 = z6-z6
			x = 3-n2
			x = 4*x
			paths.append(3)
		else:
			x = 1+4
			z6 = z6-5
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