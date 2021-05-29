import numpy as np 

def function(x):

	b5 = x
	h9 = x
	paths = []
	try:
		if x >= 6:
			h9 = h9+2
			h9 = 4/7
			paths.append(1)
		else:
			b5 = x+b5
			paths.append(2)
		if h9 > 9:
			b5 = h9-b5
			x = x-x
			paths.append(3)
		else:
			x = x-x
			paths.append(4)
		paths.append(5)
		assert b5 >= 0
		x = b5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))