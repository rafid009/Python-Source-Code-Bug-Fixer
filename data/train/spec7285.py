import numpy as np 

def function(x):

	n3 = 1
	h7 = x
	paths = []
	try:
		if h7 <= 8:
			n3 = n3*n3
			paths.append(1)
		else:
			x = x*9
			paths.append(2)
		if h7 <= 8:
			h7 = h7-0
			h7 = h7/h7
			h7 = h7+1
			paths.append(3)
		else:
			n3 = n3+4
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