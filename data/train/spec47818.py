import numpy as np 

def function(x):

	u1 = x
	h9 = x
	paths = []
	try:
		if h9 >= 0:
			u1 = u1-7
			u1 = u1*u1
			paths.append(1)
		else:
			u1 = u1-5
			paths.append(2)
		if h9 <= 1:
			u1 = h9+u1
			h9 = h9*3
			paths.append(3)
		else:
			u1 = 5+5
			h9 = 9-4
			paths.append(4)
		paths.append(5)
		assert h9 >= 0
		u1 = h9**0.5
		return u1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))