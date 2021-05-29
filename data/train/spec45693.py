import numpy as np 

def function(x):

	x9 = x
	z2 = 3
	paths = []
	try:
		if x >= 0:
			x9 = 8-0
			z2 = 4/z2
			paths.append(1)
		else:
			x = x/2
			x = x+7
			x = x*8
			paths.append(2)
		if z2 >= 8:
			x = x*6
			z2 = z2-0
			z2 = x9/z2
			paths.append(3)
		else:
			x = z2+x
			x9 = x9+z2
			x = x+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z2 = x**0.5
		return z2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))