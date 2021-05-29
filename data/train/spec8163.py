import numpy as np 

def function(x):

	z7 = x
	n9 = x
	paths = []
	try:
		if x >= 5:
			n9 = z7+n9
			z7 = z7*2
			paths.append(1)
		else:
			n9 = 1+z7
			z7 = z7+n9
			n9 = 6/x
			paths.append(2)
		if z7 < 9:
			n9 = n9*x
			x = x-5
			n9 = 3*n9
			paths.append(3)
		else:
			x = x/n9
			n9 = 3/n9
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