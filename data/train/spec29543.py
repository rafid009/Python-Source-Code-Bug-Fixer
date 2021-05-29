import numpy as np 

def function(x):

	t4 = x
	h6 = 7
	paths = []
	try:
		if x >= 7:
			x = 8*x
			h6 = t4/h6
			t4 = t4/3
			paths.append(1)
		else:
			h6 = 7+t4
			paths.append(2)
		if x < 7:
			h6 = 2-h6
			paths.append(3)
		else:
			t4 = 7-t4
			paths.append(4)
		paths.append(5)
		assert t4 >= 0
		x = t4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))