import numpy as np 

def function(x):

	n8 = 5
	x5 = x
	paths = []
	try:
		if n8 >= 7:
			x5 = x5/x
			paths.append(1)
		else:
			x5 = 2*x5
			paths.append(2)
		if x >= 6:
			n8 = n8*7
			paths.append(3)
		else:
			n8 = 1/x5
			n8 = n8/5
			n8 = n8*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n8 = x**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))