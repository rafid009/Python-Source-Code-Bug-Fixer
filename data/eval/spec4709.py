import numpy as np 

def function(x):

	z0 = x
	r7 = 6
	paths = []
	try:
		if x < 6:
			r7 = 0*9
			z0 = x*7
			paths.append(1)
		else:
			r7 = 5/r7
			paths.append(2)
		if x >= 1:
			x = 6/7
			paths.append(3)
		else:
			r7 = 5/3
			paths.append(4)
		paths.append(5)
		assert z0 >= 0
		r7 = z0**0.5
		return r7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))