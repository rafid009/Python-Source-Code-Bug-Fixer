import numpy as np 

def function(x):

	h0 = 3
	t8 = x
	paths = []
	try:
		if h0 >= 1:
			h0 = 3*h0
			paths.append(1)
		else:
			h0 = 1/3
			h0 = h0+x
			t8 = 5-t8
			paths.append(2)
		if x > 0:
			t8 = t8-0
			t8 = h0/3
			t8 = t8*8
			paths.append(3)
		else:
			t8 = x+0
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