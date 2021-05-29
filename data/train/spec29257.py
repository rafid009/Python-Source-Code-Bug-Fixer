import numpy as np 

def function(x):

	z5 = x
	z2 = 4
	paths = []
	try:
		if x > 4:
			z2 = 4/z2
			z2 = z2/z5
			paths.append(1)
		else:
			z2 = z2+x
			z5 = x+8
			x = 9-x
			paths.append(2)
		if z2 < 7:
			z5 = z5*9
			x = x*x
			x = x/x
			paths.append(3)
		else:
			x = x/z2
			x = 4+z5
			paths.append(4)
		paths.append(5)
		assert z2 >= 0
		z5 = z2**0.5
		return z5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))