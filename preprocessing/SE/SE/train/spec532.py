import numpy as np 

def function(x):

	z5 = x
	q8 = 9
	paths = []
	try:
		if z5 >= 9:
			q8 = q8+3
			paths.append(1)
		else:
			q8 = 9/5
			z5 = z5*1
			paths.append(2)
		if x <= 9:
			x = 4-x
			x = 5+x
			paths.append(3)
		else:
			z5 = 0-z5
			z5 = z5+4
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