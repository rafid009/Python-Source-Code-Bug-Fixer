import numpy as np 

def function(x):

	h9 = 5
	u1 = x
	paths = []
	try:
		if x > 6:
			x = x/1
			u1 = h9-u1
			u1 = u1-5
			paths.append(1)
		else:
			h9 = h9+u1
			x = x*3
			paths.append(2)
		if h9 > 7:
			x = 7*x
			paths.append(3)
		else:
			x = x-9
			x = 1-9
			u1 = u1/u1
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