import numpy as np 

def function(x):

	h9 = 0
	o5 = x
	paths = []
	try:
		if x >= 2:
			o5 = h9/o5
			h9 = h9*5
			h9 = h9/4
			paths.append(1)
		else:
			x = x+1
			paths.append(2)
		if h9 >= 0:
			o5 = h9+o5
			paths.append(3)
		else:
			o5 = 1*x
			h9 = x-o5
			o5 = 2-5
			paths.append(4)
		paths.append(5)
		assert o5 >= 0
		x = o5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))