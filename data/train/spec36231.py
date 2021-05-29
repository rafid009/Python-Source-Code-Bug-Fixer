import numpy as np 

def function(x):

	w5 = 5
	h9 = x
	paths = []
	try:
		if x > 5:
			h9 = w5+0
			w5 = 4/h9
			h9 = x-x
			paths.append(1)
		else:
			h9 = 0-h9
			w5 = h9-0
			paths.append(2)
		if h9 > 2:
			h9 = 4/7
			paths.append(3)
		else:
			w5 = 6/w5
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