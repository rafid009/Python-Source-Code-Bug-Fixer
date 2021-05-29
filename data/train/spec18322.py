import numpy as np 

def function(x):

	h8 = x
	h2 = x
	paths = []
	try:
		if x >= 0:
			h8 = x/5
			paths.append(1)
		else:
			h2 = x+9
			h2 = h2*x
			paths.append(2)
		if h2 > 8:
			h2 = h2-8
			h8 = h8-8
			x = 3-9
			paths.append(3)
		else:
			h8 = h8-x
			paths.append(4)
		paths.append(5)
		assert h2 >= 0
		h2 = h2**0.5
		return h2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))