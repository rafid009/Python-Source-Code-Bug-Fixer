import numpy as np 

def function(x):

	z2 = 0
	u6 = 7
	paths = []
	try:
		if x > 7:
			x = u6*4
			x = 4-x
			z2 = z2-5
			paths.append(1)
		else:
			x = 2-3
			z2 = 2+4
			z2 = z2+z2
			paths.append(2)
		if x >= 3:
			z2 = 8*4
			u6 = u6*z2
			u6 = 4+z2
			paths.append(3)
		else:
			x = 3*9
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