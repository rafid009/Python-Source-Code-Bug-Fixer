import numpy as np 

def function(x):

	n1 = 2
	h5 = x
	paths = []
	try:
		if n1 < 8:
			h5 = h5-9
			paths.append(1)
		else:
			h5 = 9/h5
			h5 = n1-h5
			x = x*3
			paths.append(2)
		if x > 1:
			x = 0/6
			h5 = 6-2
			n1 = 7-n1
			paths.append(3)
		else:
			h5 = h5+9
			n1 = x-n1
			h5 = 1/h5
			paths.append(4)
		paths.append(5)
		assert n1 >= 0
		x = n1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))