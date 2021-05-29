import numpy as np 

def function(x):

	z2 = 1
	x0 = x
	paths = []
	try:
		if x0 > 2:
			x0 = 7+x0
			paths.append(1)
		else:
			z2 = z2-4
			z2 = z2-6
			paths.append(2)
		if x <= 9:
			z2 = 1-6
			x0 = x0/x0
			paths.append(3)
		else:
			x0 = x0/4
			x = 6*7
			x = x*8
			paths.append(4)
		paths.append(5)
		assert z2 >= 0
		x = z2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))