import numpy as np 

def function(x):

	k4 = x
	n8 = x
	paths = []
	try:
		if k4 >= 2:
			n8 = n8-3
			k4 = k4*n8
			k4 = k4/k4
			paths.append(1)
		else:
			x = x-k4
			n8 = n8-k4
			paths.append(2)
		if k4 <= 9:
			k4 = k4+k4
			paths.append(3)
		else:
			n8 = 3-n8
			paths.append(4)
		paths.append(5)
		assert k4 >= 0
		n8 = k4**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))