import numpy as np 

def function(x):

	t8 = 1
	h0 = 2
	paths = []
	try:
		if t8 > 4:
			h0 = h0-2
			h0 = h0-h0
			t8 = t8*5
			paths.append(1)
		else:
			t8 = 1/t8
			t8 = t8-9
			t8 = t8*4
			paths.append(2)
		if h0 <= 8:
			h0 = h0+x
			h0 = 7/h0
			t8 = 3-8
			paths.append(3)
		else:
			h0 = 0+h0
			x = x+x
			h0 = t8+7
			paths.append(4)
		paths.append(5)
		assert t8 >= 0
		t8 = t8**0.5
		return t8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))