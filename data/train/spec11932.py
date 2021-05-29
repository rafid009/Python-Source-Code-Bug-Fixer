import numpy as np 

def function(x):

	z2 = x
	a5 = x
	x = 2
	paths = []
	try:
		if x >= 4:
			a5 = a5-z2
			paths.append(1)
		else:
			x = x+8
			paths.append(2)
		if a5 <= 3:
			x = a5+z2
			a5 = a5-a5
			z2 = z2*1
			paths.append(3)
		else:
			z2 = z2+x
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