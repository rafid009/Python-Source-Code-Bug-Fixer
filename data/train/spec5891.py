import numpy as np 

def function(x):

	a7 = x
	h0 = 3
	paths = []
	try:
		if x < 6:
			h0 = h0+4
			paths.append(1)
		else:
			x = a7+1
			paths.append(2)
		if a7 >= 8:
			a7 = x-3
			h0 = 1+h0
			h0 = h0-5
			paths.append(3)
		else:
			h0 = x*5
			a7 = a7*2
			h0 = a7/h0
			paths.append(4)
		paths.append(5)
		assert h0 >= 0
		x = h0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))