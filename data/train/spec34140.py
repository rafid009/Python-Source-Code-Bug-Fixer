import numpy as np 

def function(x):

	r9 = x
	z2 = x
	paths = []
	try:
		if r9 > 3:
			z2 = z2/8
			z2 = z2/r9
			paths.append(1)
		else:
			z2 = 2/r9
			x = 8/4
			z2 = z2*x
			paths.append(2)
		if z2 > 2:
			x = r9*r9
			r9 = r9*1
			r9 = r9/1
			paths.append(3)
		else:
			r9 = r9*r9
			r9 = x*x
			paths.append(4)
		paths.append(5)
		assert z2 >= 0
		z2 = z2**0.5
		return z2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))