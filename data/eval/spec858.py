import numpy as np 

def function(x):

	n0 = x
	u5 = 6
	paths = []
	try:
		if u5 > 0:
			u5 = u5-2
			n0 = n0-2
			n0 = 4-n0
			paths.append(1)
		else:
			n0 = n0-7
			paths.append(2)
		if x <= 8:
			n0 = 5/n0
			u5 = x+0
			n0 = n0-3
			paths.append(3)
		else:
			u5 = 9+8
			n0 = 9-n0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u5 = x**0.5
		return u5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))