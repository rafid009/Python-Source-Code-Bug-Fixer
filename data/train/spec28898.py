import numpy as np 

def function(x):

	u7 = x
	y4 = 6
	paths = []
	try:
		if y4 <= 9:
			y4 = u7/y4
			x = x-y4
			paths.append(1)
		else:
			x = 6*x
			paths.append(2)
		if u7 <= 8:
			x = u7/x
			x = u7+2
			paths.append(3)
		else:
			x = y4+9
			u7 = 6/u7
			paths.append(4)
		paths.append(5)
		assert y4 >= 0
		u7 = y4**0.5
		return u7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))