import numpy as np 

def function(x):

	x4 = 8
	n1 = 8
	paths = []
	try:
		if x < 6:
			n1 = n1/8
			x = x-x4
			x = 5*x
			paths.append(1)
		else:
			n1 = 5+n1
			paths.append(2)
		if n1 >= 6:
			x4 = x4*6
			paths.append(3)
		else:
			x4 = 8-x4
			n1 = n1/8
			n1 = n1-n1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x4 = x**0.5
		return x4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))