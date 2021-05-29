import numpy as np 

def function(x):

	r7 = x
	u4 = x
	paths = []
	try:
		if r7 >= 6:
			r7 = 7/r7
			paths.append(1)
		else:
			u4 = u4-3
			u4 = 2+u4
			paths.append(2)
		if r7 > 2:
			u4 = u4/1
			u4 = u4*x
			paths.append(3)
		else:
			r7 = 4/r7
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