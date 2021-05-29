import numpy as np 

def function(x):

	h7 = x
	e7 = 7
	x = 8
	paths = []
	try:
		if h7 >= 8:
			e7 = 0*2
			h7 = 5-h7
			paths.append(1)
		else:
			h7 = h7+7
			x = e7/x
			paths.append(2)
		if e7 < 0:
			x = 3+x
			h7 = e7/h7
			paths.append(3)
		else:
			h7 = h7/8
			x = 5-1
			paths.append(4)
		paths.append(5)
		assert h7 >= 0
		x = h7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))