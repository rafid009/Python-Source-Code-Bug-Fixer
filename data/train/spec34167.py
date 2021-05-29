import numpy as np 

def function(x):

	z2 = 1
	l2 = 5
	x = 6
	paths = []
	try:
		if z2 > 1:
			z2 = z2*9
			l2 = 8-x
			paths.append(1)
		else:
			x = x/4
			z2 = 4-8
			paths.append(2)
		if x >= 2:
			z2 = x+x
			paths.append(3)
		else:
			l2 = l2+x
			l2 = l2/7
			paths.append(4)
		paths.append(5)
		assert z2 >= 0
		z2 = z2**0.5
		return z2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))