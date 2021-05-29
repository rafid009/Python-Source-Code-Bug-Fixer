import numpy as np 

def function(x):

	h9 = 4
	w4 = x
	x = x
	paths = []
	try:
		if h9 < 4:
			x = x/x
			paths.append(1)
		else:
			h9 = h9-x
			w4 = w4*w4
			w4 = w4/7
			paths.append(2)
		if h9 > 0:
			w4 = 4-w4
			x = x*w4
			paths.append(3)
		else:
			x = x+w4
			x = x/6
			paths.append(4)
		paths.append(5)
		assert h9 >= 0
		x = h9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))