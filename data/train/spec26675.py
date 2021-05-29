import numpy as np 

def function(x):

	h2 = 0
	x9 = x
	x = x
	paths = []
	try:
		if x9 >= 7:
			h2 = 7+x
			x = 6/4
			x9 = 8+8
			paths.append(1)
		else:
			h2 = x*h2
			paths.append(2)
		if h2 < 9:
			x = 7/x
			paths.append(3)
		else:
			h2 = 9-h2
			paths.append(4)
		paths.append(5)
		assert h2 >= 0
		x9 = h2**0.5
		return x9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))