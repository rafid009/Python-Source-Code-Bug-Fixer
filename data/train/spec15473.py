import numpy as np 

def function(x):

	z1 = 4
	x5 = 1
	paths = []
	try:
		if x5 <= 7:
			x5 = 9+x
			z1 = 3-5
			x = 6-x
			paths.append(1)
		else:
			x = x+4
			x = x/8
			paths.append(2)
		if x > 9:
			x = x+4
			x = x/x
			x5 = x5-0
			paths.append(3)
		else:
			x5 = 9+x5
			x5 = x5-3
			x = 2-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x5 = x**0.5
		return x5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))