import numpy as np 

def function(x):

	f4 = x
	y2 = x
	x = 6
	paths = []
	try:
		if x <= 7:
			y2 = 0+y2
			paths.append(1)
		else:
			f4 = 4-f4
			paths.append(2)
		if x >= 4:
			y2 = y2-x
			paths.append(3)
		else:
			x = y2/y2
			y2 = x*y2
			y2 = 7-y2
			paths.append(4)
		paths.append(5)
		assert f4 >= 0
		x = f4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))