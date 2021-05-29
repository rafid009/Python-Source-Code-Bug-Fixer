import numpy as np 

def function(x):

	u1 = 0
	h9 = 8
	paths = []
	try:
		if x <= 7:
			h9 = h9*6
			x = x/1
			paths.append(1)
		else:
			x = 7*x
			u1 = 0/x
			u1 = u1/1
			paths.append(2)
		if h9 >= 2:
			h9 = 4/x
			h9 = 0*9
			paths.append(3)
		else:
			u1 = 1+h9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u1 = x**0.5
		return u1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))