import numpy as np 

def function(x):

	h6 = x
	g8 = 7
	x = x
	paths = []
	try:
		if h6 < 2:
			x = 7+5
			h6 = h6/x
			paths.append(1)
		else:
			h6 = 6/h6
			paths.append(2)
		if x <= 1:
			x = x*0
			x = 3/x
			x = 1/g8
			paths.append(3)
		else:
			x = h6+h6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h6 = x**0.5
		return h6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))