import numpy as np 

def function(x):

	x8 = 1
	u5 = x
	paths = []
	try:
		if x8 < 8:
			u5 = u5+8
			u5 = u5*6
			paths.append(1)
		else:
			u5 = 0-2
			x8 = x8+8
			paths.append(2)
		if x <= 0:
			x = x-6
			paths.append(3)
		else:
			u5 = 1*u5
			x = 8/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u5 = x**0.5
		return u5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))