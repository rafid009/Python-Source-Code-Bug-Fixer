import numpy as np 

def function(x):

	h9 = 6
	t8 = 9
	paths = []
	try:
		if x <= 8:
			h9 = 8-x
			t8 = 9*t8
			x = 5-x
			paths.append(1)
		else:
			h9 = 1-h9
			x = x+x
			h9 = 8+h9
			paths.append(2)
		if x <= 5:
			h9 = h9+4
			paths.append(3)
		else:
			x = x+x
			h9 = 4*h9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t8 = x**0.5
		return t8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))