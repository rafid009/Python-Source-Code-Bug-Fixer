import numpy as np 

def function(x):

	y8 = x
	n1 = x
	paths = []
	try:
		if n1 >= 1:
			x = 1/y8
			y8 = 0-4
			n1 = x/9
			paths.append(1)
		else:
			y8 = y8*7
			y8 = 1/y8
			paths.append(2)
		if x >= 8:
			x = 3/x
			n1 = n1*n1
			paths.append(3)
		else:
			y8 = y8/n1
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