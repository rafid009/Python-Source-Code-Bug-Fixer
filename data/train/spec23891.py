import numpy as np 

def function(x):

	h4 = x
	e0 = 4
	paths = []
	try:
		if e0 <= 2:
			x = x-0
			x = x+0
			x = x+5
			paths.append(1)
		else:
			x = 5/x
			e0 = 5-3
			x = 2+9
			paths.append(2)
		if h4 <= 2:
			x = 7/x
			e0 = e0/5
			h4 = 1-e0
			paths.append(3)
		else:
			h4 = e0-3
			e0 = h4+e0
			paths.append(4)
		paths.append(5)
		assert h4 >= 0
		h4 = h4**0.5
		return h4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))