import numpy as np 

def function(x):

	h1 = x
	n4 = x
	paths = []
	try:
		if x >= 4:
			x = x-x
			x = h1*8
			paths.append(1)
		else:
			n4 = n4/x
			paths.append(2)
		if n4 >= 0:
			n4 = 2/x
			paths.append(3)
		else:
			x = x/5
			n4 = n4/x
			paths.append(4)
		paths.append(5)
		assert n4 >= 0
		h1 = n4**0.5
		return h1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))