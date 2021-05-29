import numpy as np 

def function(x):

	f9 = x
	h2 = x
	paths = []
	try:
		if f9 < 1:
			h2 = h2-2
			h2 = 7/h2
			x = x*8
			paths.append(1)
		else:
			x = f9*7
			h2 = 2-h2
			f9 = 5/f9
			paths.append(2)
		if h2 < 2:
			x = x-x
			x = f9-x
			x = x+3
			paths.append(3)
		else:
			h2 = 5+h2
			paths.append(4)
		paths.append(5)
		assert h2 >= 0
		h2 = h2**0.5
		return h2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))