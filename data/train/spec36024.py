import numpy as np 

def function(x):

	z2 = 9
	h7 = x
	paths = []
	try:
		if x > 3:
			z2 = 0+3
			z2 = 9-z2
			z2 = z2+8
			paths.append(1)
		else:
			x = 3+x
			z2 = x/x
			paths.append(2)
		if z2 <= 8:
			z2 = z2/z2
			paths.append(3)
		else:
			x = 1+x
			paths.append(4)
		paths.append(5)
		assert h7 >= 0
		h7 = h7**0.5
		return h7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))