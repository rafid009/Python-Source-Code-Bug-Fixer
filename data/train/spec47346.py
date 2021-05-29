import numpy as np 

def function(x):

	z9 = 1
	h7 = x
	paths = []
	try:
		if h7 < 0:
			x = x+8
			paths.append(1)
		else:
			h7 = 7*3
			paths.append(2)
		if z9 > 6:
			x = x/z9
			x = h7/5
			paths.append(3)
		else:
			x = 3-0
			x = x+h7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z9 = x**0.5
		return z9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))