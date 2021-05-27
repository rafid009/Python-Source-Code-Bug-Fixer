import numpy as np 

def function(x):

	h9 = 5
	u1 = 3
	paths = []
	try:
		if h9 > 1:
			u1 = u1*7
			u1 = 6*x
			paths.append(1)
		else:
			h9 = u1+h9
			h9 = h9+3
			paths.append(2)
		if u1 >= 4:
			h9 = h9-8
			u1 = 9+9
			paths.append(3)
		else:
			u1 = h9+u1
			h9 = h9-0
			paths.append(4)
		paths.append(5)
		assert u1 >= 0
		h9 = u1**0.5
		return h9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))