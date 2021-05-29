import numpy as np 

def function(x):

	h9 = x
	t6 = 6
	paths = []
	try:
		if h9 < 3:
			h9 = h9*9
			h9 = 7+4
			t6 = t6+t6
			paths.append(1)
		else:
			h9 = h9+h9
			paths.append(2)
		if t6 <= 2:
			t6 = t6/t6
			paths.append(3)
		else:
			h9 = 8-9
			x = x*1
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