import numpy as np 

def function(x):

	u1 = 7
	h6 = x
	paths = []
	try:
		if h6 >= 6:
			u1 = h6-8
			paths.append(1)
		else:
			x = x+h6
			h6 = h6-6
			u1 = u1+u1
			paths.append(2)
		if h6 <= 9:
			u1 = 4/5
			paths.append(3)
		else:
			h6 = h6*3
			paths.append(4)
		paths.append(5)
		assert h6 >= 0
		h6 = h6**0.5
		return h6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))