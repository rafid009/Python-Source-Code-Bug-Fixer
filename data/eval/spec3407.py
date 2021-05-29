import numpy as np 

def function(x):

	z8 = 7
	n1 = 9
	paths = []
	try:
		if x >= 8:
			n1 = n1+x
			z8 = z8-4
			n1 = 0*n1
			paths.append(1)
		else:
			z8 = 0*z8
			paths.append(2)
		if x < 3:
			z8 = 4/x
			x = 9-x
			paths.append(3)
		else:
			z8 = n1-8
			x = 5/5
			paths.append(4)
		paths.append(5)
		assert z8 >= 0
		n1 = z8**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))