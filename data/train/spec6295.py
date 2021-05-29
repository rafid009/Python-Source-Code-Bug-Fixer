import numpy as np 

def function(x):

	l3 = 5
	h4 = x
	x = x
	paths = []
	try:
		if h4 < 3:
			l3 = l3/4
			h4 = h4-1
			paths.append(1)
		else:
			h4 = 3*h4
			h4 = h4*h4
			h4 = x-2
			paths.append(2)
		if x > 7:
			h4 = h4-9
			x = x/1
			x = h4/x
			paths.append(3)
		else:
			x = 1/x
			l3 = x-l3
			paths.append(4)
		paths.append(5)
		assert l3 >= 0
		h4 = l3**0.5
		return h4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))