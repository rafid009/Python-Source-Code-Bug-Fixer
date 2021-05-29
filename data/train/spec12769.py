import numpy as np 

def function(x):

	o7 = 6
	u7 = x
	x = 1
	paths = []
	try:
		if u7 < 2:
			o7 = u7/o7
			u7 = u7-7
			paths.append(1)
		else:
			x = 9*8
			paths.append(2)
		if x > 0:
			o7 = o7*7
			x = u7/x
			paths.append(3)
		else:
			x = 0-x
			o7 = o7/8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u7 = x**0.5
		return u7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))