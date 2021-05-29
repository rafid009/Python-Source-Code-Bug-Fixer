import numpy as np 

def function(x):

	q0 = 7
	u9 = x
	paths = []
	try:
		if u9 >= 6:
			q0 = u9-x
			paths.append(1)
		else:
			u9 = u9*4
			x = x-x
			paths.append(2)
		if q0 >= 2:
			q0 = q0-x
			paths.append(3)
		else:
			x = 8+6
			paths.append(4)
		paths.append(5)
		assert u9 >= 0
		u9 = u9**0.5
		return u9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))