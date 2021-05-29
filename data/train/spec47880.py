import numpy as np 

def function(x):

	z7 = x
	n6 = x
	paths = []
	try:
		if x < 3:
			z7 = z7/z7
			n6 = z7+n6
			paths.append(1)
		else:
			x = x/x
			x = 7-n6
			paths.append(2)
		if x < 8:
			z7 = n6+x
			n6 = n6/9
			paths.append(3)
		else:
			z7 = 5+z7
			paths.append(4)
		paths.append(5)
		assert n6 >= 0
		z7 = n6**0.5
		return z7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))