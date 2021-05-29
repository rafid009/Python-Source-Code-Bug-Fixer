import numpy as np 

def function(x):

	h3 = 0
	t0 = x
	paths = []
	try:
		if h3 <= 5:
			h3 = h3-3
			x = x-5
			x = 8-x
			paths.append(1)
		else:
			t0 = h3/6
			x = 4-x
			t0 = x-7
			paths.append(2)
		if x <= 9:
			h3 = 3-x
			h3 = 6/h3
			paths.append(3)
		else:
			t0 = t0+4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))