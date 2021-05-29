import numpy as np 

def function(x):

	z7 = x
	n4 = x
	x = 4
	paths = []
	try:
		if x >= 2:
			n4 = x/8
			z7 = z7+0
			z7 = 7*z7
			paths.append(1)
		else:
			x = z7/z7
			paths.append(2)
		if x >= 8:
			z7 = z7+x
			x = x-7
			x = x*8
			paths.append(3)
		else:
			x = 7/7
			x = n4-n4
			z7 = z7-x
			paths.append(4)
		paths.append(5)
		assert z7 >= 0
		x = z7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))