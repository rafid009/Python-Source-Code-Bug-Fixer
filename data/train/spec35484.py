import numpy as np 

def function(x):

	m1 = 6
	h8 = x
	paths = []
	try:
		if h8 < 6:
			x = x/2
			paths.append(1)
		else:
			m1 = h8/h8
			h8 = 9/h8
			paths.append(2)
		if x < 6:
			x = 7+7
			paths.append(3)
		else:
			h8 = 3+h8
			h8 = h8+h8
			m1 = 6*x
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