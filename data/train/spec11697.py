import numpy as np 

def function(x):

	y2 = x
	u7 = x
	paths = []
	try:
		if x > 7:
			y2 = 9*9
			paths.append(1)
		else:
			y2 = y2+2
			x = y2*3
			paths.append(2)
		if y2 < 0:
			u7 = u7/x
			u7 = u7-1
			y2 = 3*6
			paths.append(3)
		else:
			y2 = y2*6
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