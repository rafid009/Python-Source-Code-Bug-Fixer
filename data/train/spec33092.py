import numpy as np 

def function(x):

	h9 = x
	m3 = 3
	paths = []
	try:
		if m3 >= 8:
			h9 = h9*m3
			h9 = 7/5
			paths.append(1)
		else:
			h9 = h9/h9
			h9 = h9+1
			paths.append(2)
		if m3 <= 9:
			h9 = h9+5
			h9 = h9+0
			paths.append(3)
		else:
			x = x-9
			x = x+5
			x = x+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h9 = x**0.5
		return h9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))