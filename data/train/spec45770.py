import numpy as np 

def function(x):

	h7 = 9
	e6 = 2
	paths = []
	try:
		if e6 >= 2:
			h7 = h7/7
			x = h7-x
			paths.append(1)
		else:
			h7 = h7*7
			paths.append(2)
		if h7 > 1:
			h7 = h7*7
			e6 = e6/e6
			paths.append(3)
		else:
			h7 = e6+h7
			x = e6-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))