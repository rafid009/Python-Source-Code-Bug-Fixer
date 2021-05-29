import numpy as np 

def function(x):

	n7 = x
	h5 = 4
	x = 3
	paths = []
	try:
		if n7 <= 6:
			h5 = 0-1
			paths.append(1)
		else:
			n7 = n7/8
			paths.append(2)
		if x >= 4:
			x = x*9
			n7 = n7-1
			paths.append(3)
		else:
			n7 = 9*5
			paths.append(4)
		paths.append(5)
		assert h5 >= 0
		n7 = h5**0.5
		return n7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))