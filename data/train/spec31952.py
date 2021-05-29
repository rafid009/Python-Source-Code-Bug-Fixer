import numpy as np 

def function(x):

	z9 = 8
	k8 = x
	paths = []
	try:
		if x <= 4:
			z9 = k8/2
			k8 = k8/1
			x = x+6
			paths.append(1)
		else:
			z9 = x-1
			z9 = k8*z9
			paths.append(2)
		if x >= 3:
			x = x*3
			z9 = 4+z9
			paths.append(3)
		else:
			x = 5/x
			x = x+x
			k8 = z9/k8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))