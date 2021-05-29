import numpy as np 

def function(x):

	y2 = 1
	u5 = x
	paths = []
	try:
		if x <= 6:
			y2 = y2+8
			paths.append(1)
		else:
			u5 = x/u5
			u5 = u5+6
			paths.append(2)
		if x <= 6:
			y2 = y2*5
			x = 9/x
			y2 = u5+3
			paths.append(3)
		else:
			x = 8+9
			paths.append(4)
		paths.append(5)
		assert u5 >= 0
		u5 = u5**0.5
		return u5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))