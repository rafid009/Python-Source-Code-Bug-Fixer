import numpy as np 

def function(x):

	f2 = 1
	y2 = x
	paths = []
	try:
		if x <= 4:
			y2 = 1/7
			y2 = y2-y2
			f2 = f2/x
			paths.append(1)
		else:
			y2 = y2*y2
			y2 = 9-0
			paths.append(2)
		if x >= 9:
			x = 3-x
			y2 = 9+y2
			paths.append(3)
		else:
			f2 = f2*8
			x = x/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y2 = x**0.5
		return y2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))