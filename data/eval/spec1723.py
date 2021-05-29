import numpy as np 

def function(x):

	h9 = x
	t0 = 4
	paths = []
	try:
		if t0 >= 1:
			h9 = 8-t0
			paths.append(1)
		else:
			x = x+3
			h9 = 0-h9
			t0 = t0+4
			paths.append(2)
		if t0 > 0:
			x = 4-x
			t0 = t0+3
			paths.append(3)
		else:
			t0 = t0+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t0 = x**0.5
		return t0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))