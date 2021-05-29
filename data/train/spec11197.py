import numpy as np 

def function(x):

	t2 = 8
	h9 = 1
	paths = []
	try:
		if x >= 6:
			h9 = h9-1
			t2 = 2*t2
			paths.append(1)
		else:
			h9 = 1*h9
			t2 = t2-h9
			x = 3-7
			paths.append(2)
		if h9 < 0:
			h9 = h9+7
			paths.append(3)
		else:
			h9 = h9+3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t2 = x**0.5
		return t2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))