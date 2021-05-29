import numpy as np 

def function(x):

	b7 = x
	z5 = 4
	paths = []
	try:
		if x >= 9:
			z5 = x+z5
			z5 = x/1
			paths.append(1)
		else:
			x = x*z5
			x = x-2
			paths.append(2)
		if x >= 3:
			x = 2*x
			b7 = b7*2
			paths.append(3)
		else:
			x = x*z5
			x = 4-x
			paths.append(4)
		paths.append(5)
		assert b7 >= 0
		x = b7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))