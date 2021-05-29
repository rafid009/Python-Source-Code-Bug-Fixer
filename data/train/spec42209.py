import numpy as np 

def function(x):

	h9 = 2
	p1 = 2
	x = x
	paths = []
	try:
		if p1 <= 6:
			h9 = 9+h9
			h9 = h9/x
			x = 0/4
			paths.append(1)
		else:
			x = h9*h9
			paths.append(2)
		if x <= 3:
			p1 = 6/p1
			p1 = p1*1
			x = h9-0
			paths.append(3)
		else:
			h9 = 4/h9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h9 = x**0.5
		return h9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))