import numpy as np 

def function(x):

	x9 = 9
	n1 = 0
	paths = []
	try:
		if x9 < 5:
			x9 = x9-4
			paths.append(1)
		else:
			x9 = x/9
			x = 2*x
			x9 = 4*x9
			paths.append(2)
		if x >= 7:
			x9 = 0-x9
			paths.append(3)
		else:
			x9 = x9*n1
			n1 = 9+n1
			paths.append(4)
		paths.append(5)
		assert x9 >= 0
		n1 = x9**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))