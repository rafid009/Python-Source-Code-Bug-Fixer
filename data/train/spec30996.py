import numpy as np 

def function(x):

	h8 = 7
	i3 = 4
	paths = []
	try:
		if h8 <= 4:
			h8 = h8*x
			h8 = h8/3
			paths.append(1)
		else:
			h8 = h8-2
			x = 6/x
			paths.append(2)
		if i3 < 8:
			x = i3+x
			paths.append(3)
		else:
			h8 = 9/3
			x = 0/i3
			h8 = h8+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h8 = x**0.5
		return h8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))