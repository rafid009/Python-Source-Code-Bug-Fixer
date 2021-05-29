import numpy as np 

def function(x):

	z7 = x
	r9 = 1
	paths = []
	try:
		if r9 >= 9:
			r9 = 5-4
			paths.append(1)
		else:
			x = x+3
			z7 = z7-z7
			x = 3/x
			paths.append(2)
		if r9 < 1:
			x = 6-z7
			z7 = z7-r9
			paths.append(3)
		else:
			x = x/5
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