import numpy as np 

def function(x):

	f6 = x
	y0 = 1
	paths = []
	try:
		if f6 < 0:
			y0 = y0/f6
			y0 = 7+y0
			x = y0-x
			paths.append(1)
		else:
			f6 = f6-f6
			paths.append(2)
		if x >= 9:
			f6 = 3-6
			paths.append(3)
		else:
			y0 = x+4
			f6 = f6-2
			x = x-2
			paths.append(4)
		paths.append(5)
		assert f6 >= 0
		y0 = f6**0.5
		return y0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))