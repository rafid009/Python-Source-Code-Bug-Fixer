import numpy as np 

def function(x):

	k0 = 2
	z6 = 2
	x = x
	paths = []
	try:
		if x > 7:
			z6 = z6*z6
			paths.append(1)
		else:
			k0 = k0-z6
			z6 = 9/z6
			k0 = k0/1
			paths.append(2)
		if x > 2:
			z6 = z6+k0
			x = 3/1
			x = x/6
			paths.append(3)
		else:
			k0 = 4+k0
			k0 = k0*x
			paths.append(4)
		paths.append(5)
		assert k0 >= 0
		x = k0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))