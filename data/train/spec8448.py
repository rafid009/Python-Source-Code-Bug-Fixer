import numpy as np 

def function(x):

	h5 = 8
	g1 = x
	paths = []
	try:
		if h5 <= 7:
			h5 = 9+4
			paths.append(1)
		else:
			g1 = 5-9
			paths.append(2)
		if x < 8:
			x = x*h5
			g1 = g1*5
			h5 = x-4
			paths.append(3)
		else:
			x = x/g1
			h5 = h5-9
			paths.append(4)
		paths.append(5)
		assert g1 >= 0
		x = g1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))