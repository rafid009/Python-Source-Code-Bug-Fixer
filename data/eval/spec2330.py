import numpy as np 

def function(x):

	t5 = x
	h9 = 3
	paths = []
	try:
		if x > 8:
			t5 = t5/6
			h9 = 7-h9
			paths.append(1)
		else:
			h9 = h9/4
			paths.append(2)
		if t5 < 2:
			x = x-6
			h9 = h9+4
			paths.append(3)
		else:
			h9 = 9*6
			x = x/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t5 = x**0.5
		return t5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))