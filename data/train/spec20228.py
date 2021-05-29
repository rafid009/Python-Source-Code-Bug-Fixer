import numpy as np 

def function(x):

	u2 = 4
	y2 = 9
	paths = []
	try:
		if y2 > 5:
			y2 = 8+y2
			paths.append(1)
		else:
			x = 7/x
			x = x*y2
			paths.append(2)
		if u2 >= 6:
			y2 = y2+3
			paths.append(3)
		else:
			y2 = 9+y2
			u2 = 5-9
			x = 8-x
			paths.append(4)
		paths.append(5)
		assert u2 >= 0
		y2 = u2**0.5
		return y2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))