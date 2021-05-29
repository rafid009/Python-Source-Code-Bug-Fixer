import numpy as np 

def function(x):

	z1 = x
	k8 = x
	x = 8
	paths = []
	try:
		if z1 < 3:
			z1 = x*z1
			z1 = z1/9
			k8 = k8-5
			paths.append(1)
		else:
			x = k8*x
			paths.append(2)
		if x >= 0:
			x = x+5
			x = z1/x
			paths.append(3)
		else:
			z1 = 9*8
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