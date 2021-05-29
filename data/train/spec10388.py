import numpy as np 

def function(x):

	q3 = x
	h8 = x
	paths = []
	try:
		if x >= 9:
			h8 = 9/h8
			paths.append(1)
		else:
			h8 = x*2
			paths.append(2)
		if h8 < 7:
			x = 8*x
			paths.append(3)
		else:
			x = 1*5
			x = h8/8
			paths.append(4)
		paths.append(5)
		assert h8 >= 0
		h8 = h8**0.5
		return h8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))