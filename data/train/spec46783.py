import numpy as np 

def function(x):

	h6 = x
	t3 = 1
	paths = []
	try:
		if h6 < 4:
			x = 3-h6
			t3 = 4+x
			x = x-3
			paths.append(1)
		else:
			x = x/8
			t3 = 4/t3
			paths.append(2)
		if h6 >= 4:
			h6 = h6*8
			paths.append(3)
		else:
			x = h6-x
			t3 = t3-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t3 = x**0.5
		return t3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))