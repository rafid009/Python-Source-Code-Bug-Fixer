import numpy as np 

def function(x):

	o1 = x
	u4 = 9
	x = 7
	paths = []
	try:
		if o1 < 0:
			u4 = 3*u4
			u4 = u4/x
			o1 = o1+5
			paths.append(1)
		else:
			u4 = 2-u4
			paths.append(2)
		if u4 > 1:
			u4 = 8+o1
			u4 = u4/u4
			u4 = 0-u4
			paths.append(3)
		else:
			o1 = 3+o1
			x = u4-x
			u4 = 0-u4
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