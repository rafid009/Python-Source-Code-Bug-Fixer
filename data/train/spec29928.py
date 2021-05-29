import numpy as np 

def function(x):

	x7 = 8
	p8 = x
	paths = []
	try:
		if x >= 9:
			x = x+x
			paths.append(1)
		else:
			x7 = p8*p8
			x7 = 1-x
			paths.append(2)
		if x < 6:
			x7 = x7/4
			x7 = x7/x7
			paths.append(3)
		else:
			x = x-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x7 = x**0.5
		return x7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))