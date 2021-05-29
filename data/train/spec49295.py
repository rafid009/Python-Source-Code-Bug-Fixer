import numpy as np 

def function(x):

	h9 = 5
	e0 = x
	x = 6
	paths = []
	try:
		if h9 > 2:
			e0 = x-e0
			h9 = h9/8
			x = 4/6
			paths.append(1)
		else:
			e0 = 8+e0
			e0 = e0-7
			paths.append(2)
		if h9 < 6:
			h9 = 9/h9
			h9 = x*1
			paths.append(3)
		else:
			h9 = x*8
			x = x+8
			e0 = e0*7
			paths.append(4)
		paths.append(5)
		assert e0 >= 0
		x = e0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))