import numpy as np 

def function(x):

	z5 = 2
	n2 = x
	paths = []
	try:
		if z5 > 6:
			n2 = n2/8
			n2 = 4+n2
			x = 6/z5
			paths.append(1)
		else:
			n2 = n2*z5
			x = 7-x
			n2 = 4*n2
			paths.append(2)
		if n2 > 3:
			n2 = 0+n2
			x = 6/3
			paths.append(3)
		else:
			z5 = z5+0
			n2 = n2*5
			paths.append(4)
		paths.append(5)
		assert n2 >= 0
		x = n2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))