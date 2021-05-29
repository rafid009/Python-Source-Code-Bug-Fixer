import numpy as np 

def function(x):

	r9 = x
	z2 = 3
	paths = []
	try:
		if x >= 7:
			z2 = z2+r9
			x = 7*x
			paths.append(1)
		else:
			r9 = r9/5
			x = x+4
			z2 = 0-4
			paths.append(2)
		if z2 <= 3:
			x = 2*7
			r9 = 5/r9
			paths.append(3)
		else:
			x = 3*r9
			r9 = r9-2
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