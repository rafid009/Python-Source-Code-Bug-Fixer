import numpy as np 

def function(x):

	z7 = 1
	x6 = 5
	paths = []
	try:
		if x6 >= 0:
			x6 = z7-3
			paths.append(1)
		else:
			x = 2/x6
			x6 = x6*8
			x = z7*8
			paths.append(2)
		if x < 1:
			z7 = 5+z7
			paths.append(3)
		else:
			x = x6/x
			x6 = x6-x
			x = 8/1
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