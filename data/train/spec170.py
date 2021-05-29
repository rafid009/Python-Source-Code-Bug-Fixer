import numpy as np 

def function(x):

	h0 = 0
	t8 = 3
	paths = []
	try:
		if x <= 8:
			h0 = 9*h0
			paths.append(1)
		else:
			t8 = 2/6
			t8 = t8*9
			paths.append(2)
		if t8 >= 5:
			t8 = t8/h0
			paths.append(3)
		else:
			x = 1/x
			t8 = 4+t8
			x = x*t8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h0 = x**0.5
		return h0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))