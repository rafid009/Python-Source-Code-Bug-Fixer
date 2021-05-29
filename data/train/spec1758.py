import numpy as np 

def function(x):

	h4 = 2
	t7 = x
	paths = []
	try:
		if x < 9:
			t7 = x-8
			paths.append(1)
		else:
			x = x+2
			x = x+7
			h4 = h4*x
			paths.append(2)
		if h4 <= 8:
			h4 = h4+h4
			t7 = 8-h4
			paths.append(3)
		else:
			t7 = x-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h4 = x**0.5
		return h4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))