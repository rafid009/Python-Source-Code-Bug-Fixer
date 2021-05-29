import numpy as np 

def function(x):

	h7 = x
	u2 = x
	x = x
	paths = []
	try:
		if u2 <= 0:
			h7 = 7-2
			paths.append(1)
		else:
			x = x+1
			paths.append(2)
		if u2 >= 8:
			h7 = h7-x
			h7 = u2-2
			x = 6-x
			paths.append(3)
		else:
			h7 = u2-h7
			h7 = x-h7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u2 = x**0.5
		return u2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))