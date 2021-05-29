import numpy as np 

def function(x):

	t0 = x
	h8 = 4
	paths = []
	try:
		if t0 < 1:
			t0 = 1*3
			t0 = t0/t0
			paths.append(1)
		else:
			t0 = x+7
			h8 = 1/h8
			h8 = t0-h8
			paths.append(2)
		if t0 < 2:
			h8 = h8-8
			paths.append(3)
		else:
			h8 = h8+7
			x = 4+8
			paths.append(4)
		paths.append(5)
		assert h8 >= 0
		h8 = h8**0.5
		return h8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))