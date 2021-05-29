import numpy as np 

def function(x):

	z9 = 3
	k8 = x
	paths = []
	try:
		if k8 > 0:
			x = x*0
			k8 = k8+3
			paths.append(1)
		else:
			x = x/k8
			z9 = z9*k8
			k8 = 0-1
			paths.append(2)
		if k8 > 6:
			x = x*k8
			k8 = k8+3
			z9 = z9-z9
			paths.append(3)
		else:
			x = x-1
			paths.append(4)
		paths.append(5)
		assert k8 >= 0
		x = k8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))