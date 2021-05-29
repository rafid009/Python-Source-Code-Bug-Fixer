import numpy as np 

def function(x):

	w5 = 6
	h7 = 5
	paths = []
	try:
		if h7 > 2:
			w5 = 4-w5
			h7 = h7/w5
			w5 = 6+w5
			paths.append(1)
		else:
			w5 = 0+w5
			h7 = h7*x
			x = x-1
			paths.append(2)
		if h7 > 5:
			h7 = 8/6
			x = x+4
			paths.append(3)
		else:
			h7 = h7+4
			h7 = 4/2
			w5 = 2-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w5 = x**0.5
		return w5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))