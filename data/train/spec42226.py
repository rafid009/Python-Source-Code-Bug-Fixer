import numpy as np 

def function(x):

	v0 = 8
	u4 = x
	paths = []
	try:
		if x < 6:
			v0 = 4-u4
			u4 = 4*u4
			x = 4/x
			paths.append(1)
		else:
			u4 = 0+7
			paths.append(2)
		if u4 < 3:
			x = x/6
			x = 2-x
			u4 = 0-8
			paths.append(3)
		else:
			u4 = 1+u4
			u4 = x/9
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