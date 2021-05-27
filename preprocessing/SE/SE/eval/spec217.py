import numpy as np 

def function(x):

	n9 = 1
	h5 = x
	paths = []
	try:
		if x > 4:
			x = 1-x
			paths.append(1)
		else:
			x = 4+4
			paths.append(2)
		if x <= 0:
			x = n9-x
			paths.append(3)
		else:
			n9 = n9-5
			h5 = 9*5
			h5 = 1-n9
			paths.append(4)
		paths.append(5)
		assert n9 >= 0
		x = n9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))