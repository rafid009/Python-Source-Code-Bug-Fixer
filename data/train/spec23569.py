import numpy as np 

def function(x):

	x2 = 8
	z7 = 0
	paths = []
	try:
		if x >= 2:
			x2 = 0-x2
			paths.append(1)
		else:
			z7 = 1-2
			paths.append(2)
		if x2 > 7:
			x2 = x2*2
			x = x*x
			paths.append(3)
		else:
			x = 7+0
			z7 = 3+z7
			x = x-7
			paths.append(4)
		paths.append(5)
		assert z7 >= 0
		x2 = z7**0.5
		return x2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))