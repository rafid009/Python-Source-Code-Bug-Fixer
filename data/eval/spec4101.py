import numpy as np 

def function(x):

	h0 = x
	n1 = 4
	paths = []
	try:
		if x >= 2:
			h0 = 7+h0
			n1 = n1-n1
			h0 = 5-6
			paths.append(1)
		else:
			h0 = 1+h0
			paths.append(2)
		if h0 > 6:
			h0 = 8-9
			x = 6-7
			paths.append(3)
		else:
			x = 5-x
			x = x+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n1 = x**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))