import numpy as np 

def function(x):

	u4 = 6
	f4 = x
	paths = []
	try:
		if u4 <= 7:
			f4 = 8/x
			u4 = 9+u4
			u4 = u4+7
			paths.append(1)
		else:
			x = x*4
			paths.append(2)
		if f4 > 2:
			u4 = 6+6
			u4 = 8-9
			f4 = f4+8
			paths.append(3)
		else:
			u4 = x*u4
			x = 8*f4
			f4 = 4*f4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u4 = x**0.5
		return u4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))