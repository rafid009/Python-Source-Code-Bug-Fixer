import numpy as np 

def function(x):

	u4 = x
	u1 = 2
	paths = []
	try:
		if u4 < 5:
			x = x+6
			u4 = 2/u4
			u4 = u4+5
			paths.append(1)
		else:
			x = x-x
			u1 = u1/5
			paths.append(2)
		if u4 >= 4:
			u1 = 8*1
			paths.append(3)
		else:
			u4 = 9/u4
			u1 = 3+u1
			x = 3/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u1 = x**0.5
		return u1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))