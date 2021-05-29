import numpy as np 

def function(x):

	k8 = 3
	z9 = 7
	paths = []
	try:
		if z9 > 0:
			x = x/1
			z9 = z9+8
			x = 0-x
			paths.append(1)
		else:
			x = x*k8
			z9 = k8/z9
			paths.append(2)
		if k8 > 8:
			k8 = z9/4
			paths.append(3)
		else:
			k8 = k8-1
			z9 = z9/k8
			k8 = 6/k8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k8 = x**0.5
		return k8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))