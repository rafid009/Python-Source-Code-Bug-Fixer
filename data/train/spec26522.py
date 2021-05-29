import numpy as np 

def function(x):

	j0 = x
	h9 = 0
	paths = []
	try:
		if h9 >= 9:
			h9 = 2+h9
			h9 = h9+1
			paths.append(1)
		else:
			x = x+x
			paths.append(2)
		if h9 <= 1:
			j0 = j0-2
			paths.append(3)
		else:
			x = 4*x
			h9 = h9-9
			x = x-4
			paths.append(4)
		paths.append(5)
		assert j0 >= 0
		x = j0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))