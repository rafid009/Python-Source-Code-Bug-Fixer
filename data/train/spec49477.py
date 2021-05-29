import numpy as np 

def function(x):

	h6 = 4
	t5 = x
	paths = []
	try:
		if t5 >= 3:
			h6 = 5-x
			h6 = t5/3
			paths.append(1)
		else:
			h6 = 3-h6
			t5 = 0-t5
			paths.append(2)
		if h6 < 8:
			h6 = h6*t5
			paths.append(3)
		else:
			t5 = 6-3
			t5 = t5/x
			paths.append(4)
		paths.append(5)
		assert h6 >= 0
		h6 = h6**0.5
		return h6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))