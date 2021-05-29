import numpy as np 

def function(x):

	h0 = 5
	t5 = 3
	paths = []
	try:
		if x < 7:
			x = x*7
			t5 = 4-5
			paths.append(1)
		else:
			x = 1-t5
			h0 = 6*h0
			t5 = 7-9
			paths.append(2)
		if x >= 7:
			x = 2/2
			x = t5*3
			h0 = h0*6
			paths.append(3)
		else:
			t5 = 2/3
			t5 = 0/h0
			paths.append(4)
		paths.append(5)
		assert t5 >= 0
		h0 = t5**0.5
		return h0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))