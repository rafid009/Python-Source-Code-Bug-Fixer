import numpy as np 

def function(x):

	h0 = x
	a8 = 1
	paths = []
	try:
		if a8 <= 5:
			x = 4+x
			a8 = a8+a8
			paths.append(1)
		else:
			x = 8*7
			paths.append(2)
		if x < 9:
			a8 = a8+8
			h0 = 4-h0
			paths.append(3)
		else:
			x = 1/h0
			x = 0-h0
			a8 = 7*8
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