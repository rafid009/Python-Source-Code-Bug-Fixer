import numpy as np 

def function(x):

	t2 = 4
	h8 = 4
	paths = []
	try:
		if h8 <= 7:
			t2 = 8-5
			x = 4*x
			h8 = h8-5
			paths.append(1)
		else:
			x = 6-7
			x = 0-t2
			h8 = h8/2
			paths.append(2)
		if h8 >= 7:
			x = 3/t2
			paths.append(3)
		else:
			t2 = 4/t2
			h8 = h8+1
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