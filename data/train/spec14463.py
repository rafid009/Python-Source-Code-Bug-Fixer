import numpy as np 

def function(x):

	h0 = 7
	a4 = x
	x = x
	paths = []
	try:
		if x >= 4:
			x = 8-4
			paths.append(1)
		else:
			x = x+5
			h0 = h0+0
			paths.append(2)
		if a4 <= 4:
			h0 = 7+6
			a4 = a4*2
			paths.append(3)
		else:
			a4 = a4/7
			x = 5/x
			h0 = 6-h0
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