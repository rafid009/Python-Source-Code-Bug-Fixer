import numpy as np 

def function(x):

	h3 = 3
	t9 = x
	paths = []
	try:
		if x < 9:
			t9 = t9/2
			h3 = h3-4
			t9 = t9-x
			paths.append(1)
		else:
			h3 = x*2
			paths.append(2)
		if x >= 1:
			h3 = t9-h3
			t9 = 8/4
			x = 7/h3
			paths.append(3)
		else:
			h3 = 8+h3
			t9 = 3/x
			paths.append(4)
		paths.append(5)
		assert h3 >= 0
		x = h3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))