import numpy as np 

def function(x):

	h1 = 7
	t9 = 6
	paths = []
	try:
		if t9 <= 8:
			t9 = t9-t9
			t9 = t9*7
			h1 = 0-x
			paths.append(1)
		else:
			x = 2/2
			paths.append(2)
		if h1 >= 5:
			h1 = t9+0
			t9 = t9*h1
			h1 = h1-2
			paths.append(3)
		else:
			h1 = 9+0
			x = t9-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))