import numpy as np 

def function(x):

	u1 = x
	h3 = x
	x = x
	paths = []
	try:
		if x >= 8:
			h3 = 3-u1
			paths.append(1)
		else:
			u1 = 5/u1
			h3 = 7/u1
			u1 = 1+7
			paths.append(2)
		if x > 7:
			x = u1-x
			paths.append(3)
		else:
			h3 = 6-3
			paths.append(4)
		paths.append(5)
		assert h3 >= 0
		u1 = h3**0.5
		return u1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))