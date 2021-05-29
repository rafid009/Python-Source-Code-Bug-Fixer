import numpy as np 

def function(x):

	w7 = 5
	h9 = x
	paths = []
	try:
		if h9 <= 7:
			x = x*4
			w7 = 3+8
			x = x-3
			paths.append(1)
		else:
			x = x*0
			h9 = x/h9
			paths.append(2)
		if w7 >= 2:
			x = x+5
			w7 = w7-1
			x = 6-x
			paths.append(3)
		else:
			w7 = w7-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h9 = x**0.5
		return h9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))