import numpy as np 

def function(x):

	w7 = x
	z4 = x
	paths = []
	try:
		if z4 >= 0:
			w7 = 6-z4
			paths.append(1)
		else:
			x = w7+1
			w7 = w7/1
			x = x+3
			paths.append(2)
		if x <= 4:
			z4 = z4*4
			paths.append(3)
		else:
			z4 = w7*7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z4 = x**0.5
		return z4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))