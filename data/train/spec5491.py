import numpy as np 

def function(x):

	i0 = x
	h9 = x
	paths = []
	try:
		if h9 > 5:
			x = x*h9
			paths.append(1)
		else:
			x = x-9
			i0 = 7*i0
			paths.append(2)
		if h9 > 4:
			x = h9/9
			i0 = i0-3
			paths.append(3)
		else:
			h9 = i0-6
			x = h9*x
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