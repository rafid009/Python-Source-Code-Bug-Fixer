import numpy as np 

def function(x):

	h2 = x
	x4 = x
	x = 2
	paths = []
	try:
		if h2 < 8:
			x = 7*3
			x = 8+1
			paths.append(1)
		else:
			h2 = 1-x4
			h2 = 9*5
			paths.append(2)
		if x >= 2:
			h2 = h2+5
			x = x4+9
			paths.append(3)
		else:
			x4 = 9/h2
			h2 = h2+x4
			x4 = 7/x4
			paths.append(4)
		paths.append(5)
		assert h2 >= 0
		x4 = h2**0.5
		return x4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))