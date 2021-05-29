import numpy as np 

def function(x):

	n4 = x
	z6 = 1
	paths = []
	try:
		if z6 <= 4:
			n4 = n4+8
			n4 = n4/7
			x = x/n4
			paths.append(1)
		else:
			z6 = 7/z6
			paths.append(2)
		if z6 <= 7:
			n4 = 3-n4
			n4 = 2/z6
			paths.append(3)
		else:
			n4 = 0/7
			x = x-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n4 = x**0.5
		return n4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))