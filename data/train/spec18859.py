import numpy as np 

def function(x):

	w1 = 3
	h8 = 9
	paths = []
	try:
		if w1 > 6:
			x = x+w1
			paths.append(1)
		else:
			h8 = 0/h8
			paths.append(2)
		if x > 7:
			w1 = 5/w1
			h8 = x/w1
			x = x/h8
			paths.append(3)
		else:
			h8 = 7+2
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