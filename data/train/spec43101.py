import numpy as np 

def function(x):

	r3 = x
	u4 = x
	paths = []
	try:
		if u4 > 9:
			r3 = 6-r3
			x = 3-x
			paths.append(1)
		else:
			x = x-4
			x = r3/x
			paths.append(2)
		if u4 > 5:
			r3 = x-2
			paths.append(3)
		else:
			x = x/3
			r3 = 9+2
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