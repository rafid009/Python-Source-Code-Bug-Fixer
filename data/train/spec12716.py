import numpy as np 

def function(x):

	r9 = 6
	u4 = x
	x = x
	paths = []
	try:
		if r9 < 2:
			r9 = 4/x
			u4 = u4/4
			paths.append(1)
		else:
			r9 = r9-0
			paths.append(2)
		if r9 <= 0:
			r9 = 3+u4
			x = 8*x
			u4 = 4-4
			paths.append(3)
		else:
			u4 = x*4
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