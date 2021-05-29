import numpy as np 

def function(x):

	h8 = 4
	w6 = x
	paths = []
	try:
		if x < 9:
			w6 = 1+0
			x = 7+x
			h8 = 3*h8
			paths.append(1)
		else:
			x = 7/9
			paths.append(2)
		if x >= 6:
			w6 = 7*h8
			x = h8*7
			w6 = 9-7
			paths.append(3)
		else:
			w6 = x+w6
			h8 = 5/w6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h8 = x**0.5
		return h8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))