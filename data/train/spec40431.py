import numpy as np 

def function(x):

	d0 = 6
	h7 = x
	paths = []
	try:
		if h7 > 6:
			h7 = h7-1
			d0 = 3+d0
			paths.append(1)
		else:
			h7 = h7*4
			h7 = 2*5
			d0 = 5-x
			paths.append(2)
		if x > 9:
			d0 = d0/x
			paths.append(3)
		else:
			x = x+h7
			h7 = h7-8
			x = x*x
			paths.append(4)
		paths.append(5)
		assert d0 >= 0
		h7 = d0**0.5
		return h7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))