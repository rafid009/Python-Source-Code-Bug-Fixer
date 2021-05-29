import numpy as np 

def function(x):

	u4 = 4
	f3 = 8
	x = x
	paths = []
	try:
		if f3 <= 4:
			x = 5/x
			paths.append(1)
		else:
			u4 = 6+8
			u4 = x-3
			paths.append(2)
		if u4 > 4:
			u4 = 9/u4
			f3 = f3+u4
			f3 = 8*f3
			paths.append(3)
		else:
			u4 = 3-u4
			x = 5-5
			x = 3*3
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