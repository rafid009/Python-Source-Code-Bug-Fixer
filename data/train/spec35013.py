import numpy as np 

def function(x):

	e0 = x
	h7 = 3
	paths = []
	try:
		if h7 < 3:
			e0 = h7/7
			paths.append(1)
		else:
			h7 = h7+9
			e0 = e0+2
			paths.append(2)
		if x < 7:
			e0 = e0+5
			paths.append(3)
		else:
			h7 = 8/h7
			paths.append(4)
		paths.append(5)
		assert e0 >= 0
		x = e0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))