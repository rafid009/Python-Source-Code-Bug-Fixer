import numpy as np 

def function(x):

	h9 = x
	n6 = 9
	paths = []
	try:
		if h9 > 6:
			n6 = 9/n6
			paths.append(1)
		else:
			x = x-4
			paths.append(2)
		if x < 2:
			n6 = n6-7
			x = 8*x
			paths.append(3)
		else:
			n6 = x+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n6 = x**0.5
		return n6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))