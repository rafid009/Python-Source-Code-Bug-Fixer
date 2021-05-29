import numpy as np 

def function(x):

	t1 = x
	h6 = x
	paths = []
	try:
		if x <= 5:
			h6 = 7*h6
			x = t1+6
			paths.append(1)
		else:
			h6 = 0-t1
			t1 = t1-0
			paths.append(2)
		if x <= 7:
			t1 = 7+8
			paths.append(3)
		else:
			h6 = h6-h6
			t1 = t1+6
			h6 = h6*3
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