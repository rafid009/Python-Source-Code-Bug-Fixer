import numpy as np 

def function(x):

	l9 = x
	h9 = x
	paths = []
	try:
		if x > 1:
			h9 = 3*h9
			x = 3-x
			paths.append(1)
		else:
			l9 = 2-7
			paths.append(2)
		if h9 < 0:
			x = x/8
			paths.append(3)
		else:
			l9 = 5-2
			l9 = 5*h9
			paths.append(4)
		paths.append(5)
		assert l9 >= 0
		h9 = l9**0.5
		return h9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))