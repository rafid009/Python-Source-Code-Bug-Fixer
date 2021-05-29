import numpy as np 

def function(x):

	n6 = x
	z8 = 4
	paths = []
	try:
		if z8 <= 5:
			n6 = 3*n6
			n6 = 8*n6
			x = x*0
			paths.append(1)
		else:
			n6 = n6-7
			z8 = 4+z8
			paths.append(2)
		if x >= 0:
			z8 = 0/n6
			n6 = 9+n6
			n6 = n6+3
			paths.append(3)
		else:
			n6 = n6+9
			x = 7*0
			paths.append(4)
		paths.append(5)
		assert n6 >= 0
		z8 = n6**0.5
		return z8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))