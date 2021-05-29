import numpy as np 

def function(x):

	h6 = x
	d2 = 8
	paths = []
	try:
		if x <= 7:
			d2 = h6/9
			d2 = h6+d2
			paths.append(1)
		else:
			x = d2/x
			x = h6-d2
			paths.append(2)
		if d2 >= 3:
			h6 = h6*8
			h6 = h6-x
			d2 = d2/h6
			paths.append(3)
		else:
			h6 = h6-1
			paths.append(4)
		paths.append(5)
		assert d2 >= 0
		h6 = d2**0.5
		return h6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))