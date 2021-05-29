import numpy as np 

def function(x):

	n7 = x
	z7 = 8
	paths = []
	try:
		if n7 < 7:
			x = 0+x
			n7 = n7*n7
			z7 = z7/2
			paths.append(1)
		else:
			z7 = z7+3
			x = z7-x
			z7 = 5-z7
			paths.append(2)
		if n7 >= 7:
			x = n7+x
			paths.append(3)
		else:
			n7 = n7-n7
			paths.append(4)
		paths.append(5)
		assert z7 >= 0
		x = z7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))