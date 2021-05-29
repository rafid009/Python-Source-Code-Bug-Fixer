import numpy as np 

def function(x):

	n0 = 3
	z2 = x
	x = 9
	paths = []
	try:
		if x <= 8:
			n0 = n0/7
			n0 = n0-1
			z2 = z2+7
			paths.append(1)
		else:
			n0 = n0*z2
			n0 = n0/8
			paths.append(2)
		if n0 <= 9:
			x = x-n0
			x = 7/x
			paths.append(3)
		else:
			n0 = 5+n0
			z2 = n0/4
			n0 = x-n0
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