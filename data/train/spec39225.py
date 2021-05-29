import numpy as np 

def function(x):

	h9 = 8
	n3 = x
	paths = []
	try:
		if n3 > 3:
			h9 = h9*4
			n3 = n3+x
			x = x+1
			paths.append(1)
		else:
			x = n3+1
			n3 = n3+6
			n3 = 7-h9
			paths.append(2)
		if h9 > 0:
			x = x+2
			h9 = 8*h9
			paths.append(3)
		else:
			n3 = 6+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n3 = x**0.5
		return n3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))