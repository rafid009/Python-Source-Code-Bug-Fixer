import numpy as np 

def function(x):

	n6 = x
	z6 = x
	paths = []
	try:
		if n6 > 7:
			n6 = n6-4
			paths.append(1)
		else:
			x = z6/2
			n6 = 5*n6
			paths.append(2)
		if n6 < 5:
			z6 = 5*4
			x = n6*x
			x = x*7
			paths.append(3)
		else:
			z6 = 4-x
			x = z6/z6
			n6 = x+8
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