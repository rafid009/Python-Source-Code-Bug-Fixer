import numpy as np 

def function(x):

	t1 = 7
	h0 = 7
	paths = []
	try:
		if x <= 0:
			h0 = h0/1
			t1 = 4/t1
			t1 = x/h0
			paths.append(1)
		else:
			x = t1-x
			h0 = 7-3
			x = x+t1
			paths.append(2)
		if h0 < 4:
			h0 = x-h0
			x = x-3
			paths.append(3)
		else:
			t1 = t1-7
			x = x-4
			t1 = t1*h0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t1 = x**0.5
		return t1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))