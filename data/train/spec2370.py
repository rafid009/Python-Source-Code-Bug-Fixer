import numpy as np 

def function(x):

	h6 = 4
	t1 = 6
	paths = []
	try:
		if h6 < 9:
			x = x+5
			paths.append(1)
		else:
			x = x*3
			paths.append(2)
		if x >= 8:
			x = x+8
			t1 = t1*5
			paths.append(3)
		else:
			h6 = h6-6
			x = 6/x
			paths.append(4)
		paths.append(5)
		assert h6 >= 0
		x = h6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))