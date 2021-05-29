import numpy as np 

def function(x):

	z2 = 0
	n2 = x
	paths = []
	try:
		if n2 >= 1:
			n2 = n2*x
			n2 = 6*n2
			paths.append(1)
		else:
			n2 = n2-3
			z2 = 8+x
			z2 = z2-4
			paths.append(2)
		if x < 7:
			z2 = z2/8
			z2 = z2*n2
			n2 = 0/x
			paths.append(3)
		else:
			x = x+n2
			n2 = n2-2
			n2 = n2/3
			paths.append(4)
		paths.append(5)
		assert z2 >= 0
		n2 = z2**0.5
		return n2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))