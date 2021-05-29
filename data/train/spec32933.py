import numpy as np 

def function(x):

	h7 = x
	r7 = x
	paths = []
	try:
		if h7 > 1:
			r7 = 1/r7
			h7 = h7+3
			paths.append(1)
		else:
			h7 = h7*7
			x = 3+x
			x = h7+x
			paths.append(2)
		if h7 >= 5:
			x = x+3
			paths.append(3)
		else:
			x = x-4
			paths.append(4)
		paths.append(5)
		assert h7 >= 0
		r7 = h7**0.5
		return r7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))