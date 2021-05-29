import numpy as np 

def function(x):

	z5 = x
	e9 = 3
	paths = []
	try:
		if x >= 9:
			x = z5+x
			paths.append(1)
		else:
			e9 = 9+z5
			x = 5/x
			z5 = 7*z5
			paths.append(2)
		if z5 <= 6:
			e9 = e9+4
			e9 = 3-7
			z5 = 1*z5
			paths.append(3)
		else:
			x = x/6
			paths.append(4)
		paths.append(5)
		assert z5 >= 0
		e9 = z5**0.5
		return e9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))