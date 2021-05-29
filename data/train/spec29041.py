import numpy as np 

def function(x):

	r1 = 0
	u4 = x
	paths = []
	try:
		if x >= 7:
			r1 = r1*u4
			r1 = 3/4
			r1 = r1-r1
			paths.append(1)
		else:
			x = 8/x
			u4 = 1+u4
			paths.append(2)
		if x > 5:
			u4 = u4*u4
			paths.append(3)
		else:
			r1 = 1*r1
			u4 = 7-u4
			r1 = 1/2
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