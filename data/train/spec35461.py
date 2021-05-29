import numpy as np 

def function(x):

	h7 = 9
	j1 = x
	x = 4
	paths = []
	try:
		if x <= 3:
			h7 = 5-h7
			x = j1/x
			paths.append(1)
		else:
			h7 = 1/h7
			paths.append(2)
		if h7 > 0:
			x = x/2
			paths.append(3)
		else:
			h7 = 7/h7
			paths.append(4)
		paths.append(5)
		assert j1 >= 0
		h7 = j1**0.5
		return h7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))