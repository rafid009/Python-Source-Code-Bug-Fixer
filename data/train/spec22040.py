import numpy as np 

def function(x):

	k0 = 0
	z1 = 7
	paths = []
	try:
		if z1 > 7:
			z1 = z1*x
			k0 = 3-3
			x = x-9
			paths.append(1)
		else:
			x = 6+x
			k0 = 6-k0
			paths.append(2)
		if k0 > 4:
			k0 = k0+8
			paths.append(3)
		else:
			k0 = 2+z1
			z1 = z1*9
			x = x/k0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k0 = x**0.5
		return k0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))