import numpy as np 

def function(x):

	t6 = 0
	h9 = 2
	paths = []
	try:
		if h9 > 7:
			x = x+3
			paths.append(1)
		else:
			x = 1-6
			h9 = h9*x
			x = x+9
			paths.append(2)
		if h9 > 6:
			x = 8*7
			x = x+7
			h9 = 2-h9
			paths.append(3)
		else:
			x = x*2
			x = x-2
			paths.append(4)
		paths.append(5)
		assert h9 >= 0
		h9 = h9**0.5
		return h9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))