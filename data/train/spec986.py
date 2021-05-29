import numpy as np 

def function(x):

	v4 = x
	u4 = 9
	paths = []
	try:
		if x <= 3:
			v4 = 9-v4
			paths.append(1)
		else:
			u4 = u4/x
			v4 = 8-3
			paths.append(2)
		if u4 <= 2:
			u4 = 5+8
			x = x-9
			paths.append(3)
		else:
			v4 = 1*v4
			x = 7*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u4 = x**0.5
		return u4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))