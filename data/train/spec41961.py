import numpy as np 

def function(x):

	h3 = x
	t8 = x
	paths = []
	try:
		if h3 < 1:
			h3 = h3/h3
			x = 9/x
			h3 = h3*7
			paths.append(1)
		else:
			h3 = 2-h3
			paths.append(2)
		if h3 >= 1:
			x = t8/x
			h3 = 5+7
			paths.append(3)
		else:
			t8 = t8-5
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