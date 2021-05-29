import numpy as np 

def function(x):

	d8 = 8
	h0 = 9
	paths = []
	try:
		if h0 >= 4:
			x = x-d8
			paths.append(1)
		else:
			x = h0+d8
			paths.append(2)
		if h0 <= 3:
			h0 = x/1
			h0 = 5-6
			x = 5*7
			paths.append(3)
		else:
			d8 = h0/d8
			d8 = x+d8
			paths.append(4)
		paths.append(5)
		assert d8 >= 0
		h0 = d8**0.5
		return h0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))