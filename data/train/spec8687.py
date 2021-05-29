import numpy as np 

def function(x):

	u4 = 0
	g7 = 3
	paths = []
	try:
		if x < 2:
			u4 = 9*u4
			paths.append(1)
		else:
			g7 = 4+g7
			paths.append(2)
		if x > 5:
			u4 = u4/5
			paths.append(3)
		else:
			u4 = u4-0
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