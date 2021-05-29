import numpy as np 

def function(x):

	z6 = x
	w7 = 2
	paths = []
	try:
		if x <= 5:
			x = w7-z6
			paths.append(1)
		else:
			x = 8*3
			w7 = 7*8
			z6 = 7*z6
			paths.append(2)
		if x > 8:
			x = 4-x
			w7 = 5-w7
			paths.append(3)
		else:
			z6 = 0-x
			paths.append(4)
		paths.append(5)
		assert z6 >= 0
		z6 = z6**0.5
		return z6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))