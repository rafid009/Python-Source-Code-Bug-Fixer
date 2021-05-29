import numpy as np 

def function(x):

	i6 = x
	z0 = x
	paths = []
	try:
		if i6 < 8:
			i6 = i6+8
			z0 = 1+z0
			paths.append(1)
		else:
			i6 = z0+6
			x = 5/x
			paths.append(2)
		if x < 9:
			x = 2/x
			i6 = i6-4
			paths.append(3)
		else:
			x = x*2
			z0 = 1*z0
			paths.append(4)
		paths.append(5)
		assert z0 >= 0
		z0 = z0**0.5
		return z0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))