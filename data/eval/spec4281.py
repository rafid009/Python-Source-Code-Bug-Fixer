import numpy as np 

def function(x):

	k8 = x
	z0 = x
	paths = []
	try:
		if x > 8:
			k8 = 3+k8
			x = x-z0
			paths.append(1)
		else:
			x = 4*0
			k8 = k8/4
			paths.append(2)
		if z0 < 6:
			z0 = x-3
			z0 = z0/2
			paths.append(3)
		else:
			k8 = x+x
			z0 = z0+7
			x = x+z0
			paths.append(4)
		paths.append(5)
		assert k8 >= 0
		z0 = k8**0.5
		return z0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))