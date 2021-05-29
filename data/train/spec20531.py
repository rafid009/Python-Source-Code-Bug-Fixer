import numpy as np 

def function(x):

	h7 = x
	x0 = 5
	paths = []
	try:
		if x < 2:
			x0 = x0/1
			x = 9-x
			x0 = x0+x
			paths.append(1)
		else:
			h7 = h7-h7
			x0 = x*4
			h7 = x0*x0
			paths.append(2)
		if h7 > 8:
			x = x+3
			h7 = h7/h7
			x0 = x0+h7
			paths.append(3)
		else:
			x0 = 1*2
			x0 = h7-x0
			x0 = 8*x0
			paths.append(4)
		paths.append(5)
		assert x0 >= 0
		h7 = x0**0.5
		return h7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))