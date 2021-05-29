import numpy as np 

def function(x):

	k9 = x
	z0 = x
	paths = []
	try:
		if x > 9:
			k9 = 6-z0
			k9 = 3*k9
			x = k9/x
			paths.append(1)
		else:
			z0 = z0+x
			k9 = k9*4
			paths.append(2)
		if x >= 0:
			z0 = z0-x
			paths.append(3)
		else:
			k9 = k9/5
			paths.append(4)
		paths.append(5)
		assert k9 >= 0
		z0 = k9**0.5
		return z0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))