import numpy as np 

def function(x):

	z6 = x
	r9 = 1
	paths = []
	try:
		if r9 > 9:
			z6 = z6*9
			paths.append(1)
		else:
			r9 = r9-3
			paths.append(2)
		if z6 > 9:
			x = x-8
			paths.append(3)
		else:
			r9 = r9+x
			z6 = 8-9
			r9 = 8*r9
			paths.append(4)
		paths.append(5)
		assert r9 >= 0
		z6 = r9**0.5
		return z6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))