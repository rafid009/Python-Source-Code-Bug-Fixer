import numpy as np 

def function(x):

	z5 = x
	f6 = x
	paths = []
	try:
		if x <= 1:
			z5 = 1/z5
			paths.append(1)
		else:
			z5 = z5*9
			paths.append(2)
		if f6 < 4:
			x = 4/x
			paths.append(3)
		else:
			z5 = x-4
			paths.append(4)
		paths.append(5)
		assert z5 >= 0
		x = z5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))