import numpy as np 

def function(x):

	n8 = 9
	x4 = 8
	paths = []
	try:
		if x4 >= 0:
			n8 = 1/n8
			n8 = n8+7
			paths.append(1)
		else:
			x = 5/x
			x4 = n8*7
			paths.append(2)
		if x >= 2:
			n8 = n8+4
			paths.append(3)
		else:
			x4 = x4+9
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