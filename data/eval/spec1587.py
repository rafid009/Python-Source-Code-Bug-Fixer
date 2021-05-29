import numpy as np 

def function(x):

	h8 = x
	n4 = 4
	paths = []
	try:
		if h8 <= 1:
			x = h8/3
			h8 = h8*7
			n4 = 2-h8
			paths.append(1)
		else:
			x = x/x
			paths.append(2)
		if n4 >= 7:
			h8 = h8+h8
			paths.append(3)
		else:
			x = x+2
			n4 = h8*5
			x = h8-x
			paths.append(4)
		paths.append(5)
		assert h8 >= 0
		x = h8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))