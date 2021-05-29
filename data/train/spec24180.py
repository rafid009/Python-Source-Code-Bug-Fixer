import numpy as np 

def function(x):

	k8 = x
	z3 = 0
	paths = []
	try:
		if z3 > 0:
			z3 = z3*6
			paths.append(1)
		else:
			z3 = z3*7
			k8 = k8+k8
			z3 = 0-z3
			paths.append(2)
		if x >= 3:
			z3 = z3+9
			x = x/8
			paths.append(3)
		else:
			k8 = k8-5
			z3 = 7*x
			z3 = z3-1
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