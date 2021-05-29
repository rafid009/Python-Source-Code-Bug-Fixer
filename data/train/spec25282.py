import numpy as np 

def function(x):

	h3 = x
	t6 = 8
	paths = []
	try:
		if x >= 1:
			x = 0-x
			h3 = h3-1
			paths.append(1)
		else:
			t6 = 0/6
			x = x+0
			t6 = x/9
			paths.append(2)
		if h3 > 8:
			t6 = t6-8
			t6 = 8-t6
			paths.append(3)
		else:
			t6 = 1/8
			t6 = t6*9
			h3 = h3/x
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