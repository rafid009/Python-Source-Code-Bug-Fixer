import numpy as np 

def function(x):

	h8 = x
	t9 = x
	x = 6
	paths = []
	try:
		if h8 >= 9:
			x = 7*x
			x = h8+t9
			x = 6/x
			paths.append(1)
		else:
			x = x*2
			h8 = 5/h8
			paths.append(2)
		if h8 < 2:
			x = t9+2
			x = t9/x
			h8 = 7+1
			paths.append(3)
		else:
			t9 = t9/4
			t9 = t9-8
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