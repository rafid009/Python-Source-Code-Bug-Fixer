import numpy as np 

def function(x):

	u4 = x
	u0 = x
	paths = []
	try:
		if u4 < 9:
			x = x-8
			paths.append(1)
		else:
			x = u4*4
			u4 = 5*u4
			u0 = 1-u0
			paths.append(2)
		if u4 > 0:
			u4 = u0-u4
			u0 = u0-6
			paths.append(3)
		else:
			u0 = u0*u4
			paths.append(4)
		paths.append(5)
		assert u4 >= 0
		u4 = u4**0.5
		return u4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))