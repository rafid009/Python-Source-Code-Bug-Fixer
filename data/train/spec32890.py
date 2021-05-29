import numpy as np 

def function(x):

	t0 = x
	h3 = 7
	paths = []
	try:
		if x >= 7:
			h3 = h3-6
			paths.append(1)
		else:
			h3 = x+0
			paths.append(2)
		if h3 < 8:
			h3 = t0-6
			t0 = 0*t0
			t0 = t0*8
			paths.append(3)
		else:
			h3 = h3-5
			x = 8+x
			x = 6-x
			paths.append(4)
		paths.append(5)
		assert h3 >= 0
		h3 = h3**0.5
		return h3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))