import numpy as np 

def function(x):

	y5 = x
	u0 = x
	paths = []
	try:
		if u0 < 1:
			u0 = x/8
			paths.append(1)
		else:
			x = 7+x
			u0 = u0/u0
			y5 = y5+x
			paths.append(2)
		if y5 < 7:
			u0 = u0-4
			paths.append(3)
		else:
			y5 = y5*1
			x = 7/y5
			y5 = y5-y5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u0 = x**0.5
		return u0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))