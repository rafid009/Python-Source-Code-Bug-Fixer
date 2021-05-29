import numpy as np 

def function(x):

	g1 = 0
	x9 = 8
	paths = []
	try:
		if x > 8:
			x9 = g1+x9
			paths.append(1)
		else:
			x9 = 7/x9
			paths.append(2)
		if x <= 5:
			x9 = 9/x9
			paths.append(3)
		else:
			x9 = g1-8
			x = x-5
			x9 = 5+x9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x9 = x**0.5
		return x9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))