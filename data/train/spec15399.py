import numpy as np 

def function(x):

	l5 = 5
	h9 = x
	paths = []
	try:
		if h9 < 4:
			l5 = l5-1
			l5 = 8/l5
			paths.append(1)
		else:
			h9 = 1*h9
			paths.append(2)
		if h9 < 4:
			h9 = 9*4
			l5 = 3-l5
			l5 = l5-9
			paths.append(3)
		else:
			l5 = 6*l5
			h9 = h9-9
			paths.append(4)
		paths.append(5)
		assert l5 >= 0
		h9 = l5**0.5
		return h9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))