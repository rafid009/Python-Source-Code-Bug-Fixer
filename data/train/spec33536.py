import numpy as np 

def function(x):

	h9 = x
	d8 = x
	x = 4
	paths = []
	try:
		if h9 < 9:
			d8 = 6+d8
			x = x/x
			d8 = d8/5
			paths.append(1)
		else:
			h9 = 3-h9
			d8 = h9+4
			paths.append(2)
		if h9 > 8:
			h9 = 4/h9
			paths.append(3)
		else:
			x = x+5
			x = x-0
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