import numpy as np 

def function(x):

	h8 = 2
	u1 = 6
	paths = []
	try:
		if x >= 5:
			u1 = 7/x
			u1 = u1-x
			paths.append(1)
		else:
			h8 = x/h8
			paths.append(2)
		if h8 < 7:
			x = x+5
			paths.append(3)
		else:
			x = x+5
			x = 4-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u1 = x**0.5
		return u1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))