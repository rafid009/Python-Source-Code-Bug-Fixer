import numpy as np 

def function(x):

	z2 = 1
	b5 = x
	paths = []
	try:
		if z2 < 2:
			b5 = b5+1
			z2 = z2*z2
			z2 = b5-b5
			paths.append(1)
		else:
			x = 4+x
			paths.append(2)
		if z2 < 1:
			z2 = z2/x
			paths.append(3)
		else:
			x = x/8
			z2 = x/8
			paths.append(4)
		paths.append(5)
		assert b5 >= 0
		z2 = b5**0.5
		return z2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))