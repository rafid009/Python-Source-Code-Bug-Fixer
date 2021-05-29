import numpy as np 

def function(x):

	x4 = x
	u4 = 1
	paths = []
	try:
		if u4 > 3:
			x = x*3
			u4 = x+x
			paths.append(1)
		else:
			u4 = u4+8
			x = 2+x
			paths.append(2)
		if u4 > 6:
			u4 = 6/u4
			u4 = 2+6
			u4 = u4+x
			paths.append(3)
		else:
			x = x/x4
			paths.append(4)
		paths.append(5)
		assert u4 >= 0
		x4 = u4**0.5
		return x4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))