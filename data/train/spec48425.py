import numpy as np 

def function(x):

	h2 = 1
	x9 = x
	paths = []
	try:
		if h2 <= 6:
			x = x9-x9
			h2 = 8-h2
			h2 = 3/h2
			paths.append(1)
		else:
			x = x9/x
			paths.append(2)
		if h2 <= 5:
			h2 = h2+0
			paths.append(3)
		else:
			x = x*3
			paths.append(4)
		paths.append(5)
		assert x9 >= 0
		x = x9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))