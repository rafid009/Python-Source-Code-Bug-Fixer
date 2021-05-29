import numpy as np 

def function(x):

	h9 = x
	b0 = 8
	paths = []
	try:
		if h9 > 2:
			b0 = 3/b0
			x = 4*5
			h9 = 8*h9
			paths.append(1)
		else:
			h9 = 3/2
			paths.append(2)
		if x > 5:
			b0 = 8+b0
			b0 = b0/b0
			paths.append(3)
		else:
			h9 = h9-9
			paths.append(4)
		paths.append(5)
		assert h9 >= 0
		h9 = h9**0.5
		return h9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))