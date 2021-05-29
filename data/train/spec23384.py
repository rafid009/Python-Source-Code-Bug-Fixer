import numpy as np 

def function(x):

	k7 = x
	z6 = 9
	paths = []
	try:
		if x >= 0:
			k7 = k7*1
			z6 = z6/1
			paths.append(1)
		else:
			x = 7-9
			x = x+8
			k7 = k7/x
			paths.append(2)
		if z6 >= 2:
			x = 4*x
			z6 = 6+8
			z6 = k7-6
			paths.append(3)
		else:
			x = 5+x
			x = x-7
			paths.append(4)
		paths.append(5)
		assert k7 >= 0
		z6 = k7**0.5
		return z6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))