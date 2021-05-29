import numpy as np 

def function(x):

	u4 = 4
	t0 = x
	paths = []
	try:
		if t0 < 4:
			x = x-0
			u4 = 0-4
			paths.append(1)
		else:
			t0 = 7*u4
			u4 = 3+u4
			t0 = 0-u4
			paths.append(2)
		if x < 2:
			t0 = 2-7
			paths.append(3)
		else:
			u4 = x+8
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