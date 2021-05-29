import numpy as np 

def function(x):

	z6 = x
	n6 = x
	x = x
	paths = []
	try:
		if z6 <= 9:
			x = x/x
			n6 = 1*z6
			x = 7/x
			paths.append(1)
		else:
			z6 = 0-x
			n6 = n6-4
			paths.append(2)
		if n6 >= 5:
			x = x*x
			x = n6+x
			n6 = n6-4
			paths.append(3)
		else:
			z6 = x/z6
			paths.append(4)
		paths.append(5)
		assert n6 >= 0
		x = n6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))