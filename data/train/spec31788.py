import numpy as np 

def function(x):

	w5 = 2
	h6 = 8
	paths = []
	try:
		if h6 >= 1:
			h6 = x/h6
			w5 = w5/3
			w5 = w5+8
			paths.append(1)
		else:
			w5 = w5/x
			h6 = h6-h6
			paths.append(2)
		if x > 4:
			x = 6-w5
			h6 = 1/w5
			h6 = h6+8
			paths.append(3)
		else:
			h6 = h6+5
			x = x*0
			paths.append(4)
		paths.append(5)
		assert h6 >= 0
		h6 = h6**0.5
		return h6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))