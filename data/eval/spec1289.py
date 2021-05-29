import numpy as np 

def function(x):

	x6 = 2
	u4 = x
	paths = []
	try:
		if u4 > 7:
			x6 = 1+u4
			x = u4+4
			paths.append(1)
		else:
			x6 = u4/x
			x = 9+x
			x = 8-x
			paths.append(2)
		if x >= 0:
			x6 = 6+x6
			x6 = u4/x6
			paths.append(3)
		else:
			u4 = u4/u4
			x6 = x6*x6
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