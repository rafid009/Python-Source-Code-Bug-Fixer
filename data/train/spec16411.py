import numpy as np 

def function(x):

	u1 = 8
	u4 = x
	paths = []
	try:
		if x <= 1:
			x = u4+4
			u1 = u1*u1
			u4 = 5/u4
			paths.append(1)
		else:
			u4 = u4+u1
			u4 = u4-1
			u1 = 1/u1
			paths.append(2)
		if u4 >= 3:
			u1 = 0/u1
			x = u1+2
			paths.append(3)
		else:
			u4 = 9*u4
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