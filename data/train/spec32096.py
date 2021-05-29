import numpy as np 

def function(x):

	z6 = x
	z7 = 6
	paths = []
	try:
		if z7 >= 4:
			x = z6/7
			paths.append(1)
		else:
			z7 = 6-z7
			x = 6*8
			paths.append(2)
		if z7 > 1:
			x = 0*x
			x = x*3
			paths.append(3)
		else:
			z6 = 6-1
			z7 = 9*z7
			paths.append(4)
		paths.append(5)
		assert z6 >= 0
		z7 = z6**0.5
		return z7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))