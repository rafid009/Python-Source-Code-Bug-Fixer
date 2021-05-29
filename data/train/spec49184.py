import numpy as np 

def function(x):

	z4 = 3
	w3 = x
	paths = []
	try:
		if z4 <= 3:
			w3 = w3+7
			z4 = 7/z4
			paths.append(1)
		else:
			x = x/x
			z4 = z4/1
			z4 = 1-9
			paths.append(2)
		if x > 5:
			w3 = z4+w3
			x = 1*x
			z4 = z4*7
			paths.append(3)
		else:
			w3 = w3+7
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