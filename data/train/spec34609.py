import numpy as np 

def function(x):

	z7 = 7
	n7 = 3
	paths = []
	try:
		if z7 >= 7:
			z7 = n7+z7
			paths.append(1)
		else:
			x = x-1
			n7 = 1+n7
			x = 1*x
			paths.append(2)
		if n7 <= 3:
			n7 = n7-z7
			z7 = n7-4
			paths.append(3)
		else:
			z7 = 1+z7
			n7 = 4+n7
			z7 = x+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n7 = x**0.5
		return n7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))