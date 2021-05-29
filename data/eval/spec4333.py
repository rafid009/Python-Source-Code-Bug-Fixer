import numpy as np 

def function(x):

	h7 = x
	w6 = 8
	paths = []
	try:
		if h7 >= 2:
			w6 = h7+w6
			paths.append(1)
		else:
			w6 = h7*1
			paths.append(2)
		if h7 < 8:
			x = 3-h7
			x = 9/x
			x = 9*3
			paths.append(3)
		else:
			x = x-1
			w6 = w6-7
			x = 4-3
			paths.append(4)
		paths.append(5)
		assert h7 >= 0
		w6 = h7**0.5
		return w6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))