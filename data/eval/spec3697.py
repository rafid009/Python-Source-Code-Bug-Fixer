import numpy as np 

def function(x):

	h9 = x
	w1 = 2
	paths = []
	try:
		if w1 < 4:
			w1 = w1/4
			x = x*2
			w1 = w1*8
			paths.append(1)
		else:
			x = h9/8
			h9 = h9-5
			h9 = 0-9
			paths.append(2)
		if x >= 7:
			w1 = w1*x
			w1 = w1/h9
			paths.append(3)
		else:
			h9 = 1+3
			x = x*1
			w1 = h9*9
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