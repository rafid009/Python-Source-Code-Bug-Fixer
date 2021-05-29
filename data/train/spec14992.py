import numpy as np 

def function(x):

	x4 = x
	u1 = 0
	paths = []
	try:
		if x4 <= 1:
			u1 = x4/x
			x = u1/6
			paths.append(1)
		else:
			x = x-4
			x = x/x
			paths.append(2)
		if x4 < 7:
			u1 = x+8
			u1 = 6/6
			paths.append(3)
		else:
			x = u1+u1
			u1 = 0-u1
			x = x-x4
			paths.append(4)
		paths.append(5)
		assert x4 >= 0
		x4 = x4**0.5
		return x4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))