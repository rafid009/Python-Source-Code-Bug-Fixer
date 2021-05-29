import numpy as np 

def function(x):

	h7 = x
	x8 = x
	paths = []
	try:
		if h7 >= 7:
			x = 8-x
			x8 = x8+h7
			paths.append(1)
		else:
			x8 = x8/x8
			paths.append(2)
		if x >= 8:
			x8 = h7+2
			x = x+h7
			paths.append(3)
		else:
			x8 = x*x8
			h7 = x/h7
			paths.append(4)
		paths.append(5)
		assert x8 >= 0
		x = x8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))