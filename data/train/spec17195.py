import numpy as np 

def function(x):

	n7 = x
	z4 = 8
	paths = []
	try:
		if x < 9:
			x = x-z4
			n7 = 9*n7
			x = 5/n7
			paths.append(1)
		else:
			x = x-0
			n7 = 4*n7
			x = 5/n7
			paths.append(2)
		if n7 <= 0:
			n7 = n7-x
			paths.append(3)
		else:
			x = x*9
			z4 = z4/5
			n7 = 0/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))