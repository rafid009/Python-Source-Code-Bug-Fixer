import numpy as np 

def function(x):

	x6 = x
	z2 = x
	paths = []
	try:
		if z2 < 3:
			x6 = x6-x6
			x = 2*z2
			paths.append(1)
		else:
			x = x-x6
			paths.append(2)
		if x <= 4:
			x = x/7
			paths.append(3)
		else:
			z2 = 7*z2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x6 = x**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))