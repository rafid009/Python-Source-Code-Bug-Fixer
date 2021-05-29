import numpy as np 

def function(x):

	u6 = x
	n4 = x
	paths = []
	try:
		if n4 < 1:
			u6 = u6-x
			u6 = 5-u6
			paths.append(1)
		else:
			x = 8-x
			u6 = 7*5
			paths.append(2)
		if n4 < 2:
			x = 3*2
			paths.append(3)
		else:
			n4 = u6*3
			u6 = u6-u6
			paths.append(4)
		paths.append(5)
		assert n4 >= 0
		u6 = n4**0.5
		return u6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))