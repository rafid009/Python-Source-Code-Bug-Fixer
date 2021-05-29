import numpy as np 

def function(x):

	z0 = x
	r9 = x
	paths = []
	try:
		if z0 >= 7:
			z0 = r9/z0
			paths.append(1)
		else:
			z0 = 9/5
			x = r9*3
			x = 7-8
			paths.append(2)
		if x < 9:
			x = 2*x
			z0 = 9+z0
			x = 4-1
			paths.append(3)
		else:
			x = 2/9
			paths.append(4)
		paths.append(5)
		assert r9 >= 0
		x = r9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))