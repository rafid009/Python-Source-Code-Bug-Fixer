import numpy as np 

def function(x):

	a5 = x
	z2 = x
	paths = []
	try:
		if a5 < 3:
			a5 = a5-9
			paths.append(1)
		else:
			z2 = z2+9
			z2 = 4-z2
			paths.append(2)
		if z2 > 1:
			z2 = z2/5
			a5 = 5+z2
			a5 = a5*6
			paths.append(3)
		else:
			z2 = 5*z2
			x = a5-x
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		z2 = a5**0.5
		return z2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))