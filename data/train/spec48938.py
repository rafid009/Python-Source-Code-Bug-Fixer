import numpy as np 

def function(x):

	d5 = 7
	h3 = x
	paths = []
	try:
		if d5 > 7:
			x = x-h3
			h3 = 2*8
			paths.append(1)
		else:
			d5 = d5/6
			d5 = 4/d5
			h3 = x-8
			paths.append(2)
		if h3 >= 8:
			h3 = h3*4
			paths.append(3)
		else:
			h3 = h3/4
			d5 = x/h3
			h3 = 0/7
			paths.append(4)
		paths.append(5)
		assert d5 >= 0
		h3 = d5**0.5
		return h3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))