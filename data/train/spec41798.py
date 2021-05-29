import numpy as np 

def function(x):

	z0 = x
	k8 = x
	paths = []
	try:
		if z0 < 7:
			z0 = z0*3
			x = 6*x
			x = x+7
			paths.append(1)
		else:
			z0 = z0*7
			z0 = z0+0
			z0 = x/7
			paths.append(2)
		if x >= 7:
			k8 = 6+k8
			k8 = k8/k8
			paths.append(3)
		else:
			x = x*9
			paths.append(4)
		paths.append(5)
		assert z0 >= 0
		x = z0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))