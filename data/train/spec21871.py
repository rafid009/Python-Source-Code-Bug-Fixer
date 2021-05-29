import numpy as np 

def function(x):

	z2 = x
	i2 = 8
	paths = []
	try:
		if x < 6:
			i2 = 2+i2
			i2 = i2*z2
			z2 = z2+i2
			paths.append(1)
		else:
			z2 = 6+z2
			z2 = z2-z2
			paths.append(2)
		if i2 <= 9:
			i2 = z2-8
			paths.append(3)
		else:
			z2 = z2+4
			z2 = i2+z2
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