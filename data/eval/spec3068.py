import numpy as np 

def function(x):

	u7 = 1
	c6 = 3
	paths = []
	try:
		if u7 < 8:
			u7 = u7*8
			paths.append(1)
		else:
			x = 5-x
			u7 = u7*4
			u7 = u7-9
			paths.append(2)
		if u7 < 0:
			u7 = u7-u7
			x = 9-x
			paths.append(3)
		else:
			x = 7/x
			u7 = x+4
			paths.append(4)
		paths.append(5)
		assert u7 >= 0
		x = u7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))