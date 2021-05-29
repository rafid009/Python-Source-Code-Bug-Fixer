import numpy as np 

def function(x):

	z7 = 0
	a8 = x
	paths = []
	try:
		if a8 >= 1:
			x = 0*x
			z7 = z7*7
			paths.append(1)
		else:
			a8 = a8*x
			paths.append(2)
		if z7 <= 6:
			a8 = x/3
			paths.append(3)
		else:
			x = x-8
			a8 = 1-a8
			paths.append(4)
		paths.append(5)
		assert a8 >= 0
		x = a8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))