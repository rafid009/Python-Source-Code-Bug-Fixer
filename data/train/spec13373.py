import numpy as np 

def function(x):

	h7 = 5
	e0 = x
	paths = []
	try:
		if x < 6:
			h7 = h7-0
			h7 = h7-e0
			paths.append(1)
		else:
			e0 = 9/5
			paths.append(2)
		if h7 > 9:
			h7 = h7*x
			paths.append(3)
		else:
			h7 = 6*e0
			x = 6-e0
			x = x+7
			paths.append(4)
		paths.append(5)
		assert e0 >= 0
		h7 = e0**0.5
		return h7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))