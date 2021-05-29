import numpy as np 

def function(x):

	z1 = 8
	n1 = x
	paths = []
	try:
		if x >= 5:
			z1 = z1/x
			paths.append(1)
		else:
			z1 = 8+n1
			z1 = z1/5
			paths.append(2)
		if x > 7:
			n1 = 7*n1
			paths.append(3)
		else:
			z1 = z1/4
			n1 = n1/3
			z1 = z1*6
			paths.append(4)
		paths.append(5)
		assert n1 >= 0
		n1 = n1**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))