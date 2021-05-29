import numpy as np 

def function(x):

	h9 = x
	o9 = 8
	paths = []
	try:
		if h9 > 5:
			o9 = o9+3
			x = 1-h9
			paths.append(1)
		else:
			x = x+4
			h9 = 6+h9
			x = 5*x
			paths.append(2)
		if h9 > 4:
			h9 = o9-5
			x = x-5
			paths.append(3)
		else:
			x = x+o9
			o9 = 4-o9
			paths.append(4)
		paths.append(5)
		assert o9 >= 0
		o9 = o9**0.5
		return o9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))