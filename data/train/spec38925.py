import numpy as np 

def function(x):

	h3 = 4
	t4 = x
	paths = []
	try:
		if t4 > 7:
			t4 = 7/t4
			paths.append(1)
		else:
			h3 = 0/h3
			x = x*3
			paths.append(2)
		if h3 >= 1:
			t4 = x/x
			paths.append(3)
		else:
			t4 = h3-h3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h3 = x**0.5
		return h3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))