import numpy as np 

def function(x):

	e8 = 8
	h7 = x
	paths = []
	try:
		if e8 < 1:
			h7 = 2-h7
			paths.append(1)
		else:
			h7 = h7*5
			h7 = h7+0
			e8 = x/e8
			paths.append(2)
		if x > 1:
			x = 5+x
			paths.append(3)
		else:
			h7 = 1/h7
			h7 = e8/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h7 = x**0.5
		return h7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))