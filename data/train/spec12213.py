import numpy as np 

def function(x):

	n2 = 8
	z2 = 5
	paths = []
	try:
		if n2 < 7:
			z2 = z2/x
			n2 = n2*9
			x = 3/x
			paths.append(1)
		else:
			n2 = 9/n2
			n2 = n2/x
			paths.append(2)
		if n2 <= 0:
			n2 = 0*n2
			paths.append(3)
		else:
			n2 = 9+z2
			n2 = n2/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))