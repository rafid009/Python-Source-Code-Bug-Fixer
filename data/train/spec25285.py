import numpy as np 

def function(x):

	k0 = x
	z4 = x
	paths = []
	try:
		if k0 <= 6:
			x = 2/8
			z4 = 2*z4
			x = k0*x
			paths.append(1)
		else:
			k0 = 3/k0
			z4 = z4-0
			paths.append(2)
		if z4 >= 3:
			k0 = k0+0
			k0 = 6-k0
			paths.append(3)
		else:
			z4 = 4/z4
			x = 7*5
			x = 3-4
			paths.append(4)
		paths.append(5)
		assert k0 >= 0
		k0 = k0**0.5
		return k0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))