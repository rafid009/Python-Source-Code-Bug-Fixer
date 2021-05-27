import numpy as np 

def function(x):

	z2 = x
	n1 = 2
	x = x
	paths = []
	try:
		if x > 3:
			n1 = n1/4
			z2 = z2/8
			paths.append(1)
		else:
			z2 = 3/z2
			x = 7*x
			paths.append(2)
		if z2 <= 0:
			z2 = 6/z2
			z2 = 2*1
			paths.append(3)
		else:
			z2 = z2-n1
			x = x-x
			n1 = z2-z2
			paths.append(4)
		paths.append(5)
		assert z2 >= 0
		x = z2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))