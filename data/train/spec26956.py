import numpy as np 

def function(x):

	h9 = 5
	d2 = x
	paths = []
	try:
		if d2 <= 5:
			x = x*x
			h9 = h9+h9
			x = 7+d2
			paths.append(1)
		else:
			x = x*8
			h9 = h9+1
			paths.append(2)
		if d2 >= 1:
			h9 = 7+7
			d2 = 7+d2
			h9 = h9+h9
			paths.append(3)
		else:
			h9 = h9-h9
			x = x-h9
			paths.append(4)
		paths.append(5)
		assert d2 >= 0
		h9 = d2**0.5
		return h9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))