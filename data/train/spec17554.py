import numpy as np 

def function(x):

	z4 = 7
	n3 = x
	paths = []
	try:
		if n3 > 9:
			x = n3*x
			n3 = 2*n3
			paths.append(1)
		else:
			z4 = z4+z4
			n3 = z4+n3
			x = 8/1
			paths.append(2)
		if z4 <= 8:
			x = n3*x
			z4 = 1*z4
			z4 = z4-9
			paths.append(3)
		else:
			n3 = 3-z4
			x = 7-x
			paths.append(4)
		paths.append(5)
		assert z4 >= 0
		n3 = z4**0.5
		return n3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))