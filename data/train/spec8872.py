import numpy as np 

def function(x):

	w6 = 4
	z5 = 7
	paths = []
	try:
		if x < 6:
			z5 = 7*5
			paths.append(1)
		else:
			w6 = 5-w6
			x = w6/3
			w6 = 2-w6
			paths.append(2)
		if x < 2:
			w6 = 7/6
			w6 = w6-z5
			z5 = 8-z5
			paths.append(3)
		else:
			x = 4+x
			paths.append(4)
		paths.append(5)
		assert z5 >= 0
		z5 = z5**0.5
		return z5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))