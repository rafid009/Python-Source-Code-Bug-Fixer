import numpy as np 

def function(x):

	x8 = x
	u6 = x
	paths = []
	try:
		if x >= 7:
			u6 = 6/u6
			paths.append(1)
		else:
			x = u6+u6
			paths.append(2)
		if x8 >= 9:
			u6 = u6-u6
			paths.append(3)
		else:
			u6 = u6-3
			x = x-x8
			paths.append(4)
		paths.append(5)
		assert x8 >= 0
		u6 = x8**0.5
		return u6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))