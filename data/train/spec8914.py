import numpy as np 

def function(x):

	j1 = x
	h6 = x
	paths = []
	try:
		if x < 1:
			h6 = 6+4
			j1 = x+8
			paths.append(1)
		else:
			x = 3/5
			h6 = h6/2
			paths.append(2)
		if x >= 3:
			x = 9+3
			j1 = j1*2
			x = j1-x
			paths.append(3)
		else:
			j1 = h6+8
			j1 = 3-h6
			h6 = 6+7
			paths.append(4)
		paths.append(5)
		assert j1 >= 0
		h6 = j1**0.5
		return h6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))