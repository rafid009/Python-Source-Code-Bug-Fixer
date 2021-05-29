import numpy as np 

def function(x):

	d8 = x
	h7 = 4
	paths = []
	try:
		if h7 < 2:
			d8 = 4/h7
			d8 = h7-1
			paths.append(1)
		else:
			x = 0/6
			h7 = h7+h7
			x = d8/8
			paths.append(2)
		if d8 > 8:
			x = 8+3
			x = 5/x
			h7 = x/1
			paths.append(3)
		else:
			x = x-6
			h7 = h7-3
			h7 = h7-6
			paths.append(4)
		paths.append(5)
		assert d8 >= 0
		d8 = d8**0.5
		return d8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))