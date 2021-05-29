import numpy as np 

def function(x):

	g8 = 1
	h9 = 5
	paths = []
	try:
		if h9 <= 8:
			h9 = h9/1
			x = x-5
			paths.append(1)
		else:
			h9 = h9-h9
			paths.append(2)
		if g8 >= 4:
			x = 0-h9
			g8 = x+g8
			x = x*9
			paths.append(3)
		else:
			g8 = x+g8
			x = h9/1
			x = x*g8
			paths.append(4)
		paths.append(5)
		assert g8 >= 0
		x = g8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))