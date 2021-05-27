import numpy as np 

def function(x):

	z0 = x
	n3 = 7
	paths = []
	try:
		if x > 7:
			n3 = n3+3
			z0 = z0*6
			paths.append(1)
		else:
			x = x+n3
			x = n3/z0
			x = 4+4
			paths.append(2)
		if n3 >= 1:
			z0 = 0-1
			paths.append(3)
		else:
			n3 = n3/9
			z0 = 1*9
			paths.append(4)
		paths.append(5)
		assert z0 >= 0
		n3 = z0**0.5
		return n3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))