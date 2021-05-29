import numpy as np 

def function(x):

	h5 = x
	d1 = x
	paths = []
	try:
		if x < 6:
			h5 = x*h5
			paths.append(1)
		else:
			h5 = 3/h5
			d1 = 1*d1
			paths.append(2)
		if h5 <= 5:
			d1 = d1*3
			d1 = 8*2
			paths.append(3)
		else:
			h5 = 3-x
			h5 = h5-d1
			h5 = x/x
			paths.append(4)
		paths.append(5)
		assert d1 >= 0
		x = d1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))