import numpy as np 

def function(x):

	x2 = x
	u2 = x
	paths = []
	try:
		if x2 < 6:
			u2 = u2*7
			x2 = 4-3
			x = 7/x
			paths.append(1)
		else:
			x2 = 4*3
			x = x+4
			u2 = u2-0
			paths.append(2)
		if x2 < 9:
			u2 = 9+u2
			u2 = 9/x
			paths.append(3)
		else:
			x2 = x2-0
			paths.append(4)
		paths.append(5)
		assert u2 >= 0
		u2 = u2**0.5
		return u2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))