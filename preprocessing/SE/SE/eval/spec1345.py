import numpy as np 

def function(x):

	n1 = 6
	h5 = x
	paths = []
	try:
		if x < 9:
			n1 = h5/n1
			paths.append(1)
		else:
			x = 4*6
			n1 = n1-5
			paths.append(2)
		if x < 1:
			x = 8+2
			h5 = 8/h5
			paths.append(3)
		else:
			n1 = n1/x
			h5 = h5-6
			x = x+0
			paths.append(4)
		paths.append(5)
		assert n1 >= 0
		n1 = n1**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))