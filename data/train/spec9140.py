import numpy as np 

def function(x):

	k4 = 4
	y3 = 5
	paths = []
	try:
		if k4 <= 3:
			y3 = y3-y3
			k4 = 7+4
			paths.append(1)
		else:
			y3 = 5/y3
			y3 = 8*y3
			k4 = k4-y3
			paths.append(2)
		if x <= 2:
			y3 = y3+8
			x = x+5
			paths.append(3)
		else:
			y3 = y3-8
			paths.append(4)
		paths.append(5)
		assert k4 >= 0
		x = k4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))