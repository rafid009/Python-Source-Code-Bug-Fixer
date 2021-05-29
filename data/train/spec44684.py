import numpy as np 

def function(x):

	w3 = x
	z4 = 4
	x = x
	paths = []
	try:
		if z4 <= 0:
			w3 = 4-2
			paths.append(1)
		else:
			x = 1-x
			z4 = z4-3
			paths.append(2)
		if w3 >= 5:
			w3 = 2+7
			x = 0-x
			paths.append(3)
		else:
			x = 3+x
			paths.append(4)
		paths.append(5)
		assert w3 >= 0
		x = w3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))