import numpy as np 

def function(x):

	w6 = x
	h0 = 9
	paths = []
	try:
		if w6 >= 2:
			x = x*w6
			paths.append(1)
		else:
			w6 = 1-1
			x = x/3
			paths.append(2)
		if x <= 1:
			h0 = h0-0
			w6 = h0-w6
			paths.append(3)
		else:
			h0 = h0/h0
			w6 = w6-8
			w6 = 4*w6
			paths.append(4)
		paths.append(5)
		assert w6 >= 0
		x = w6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))