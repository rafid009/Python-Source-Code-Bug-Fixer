import numpy as np 

def function(x):

	y2 = 6
	e4 = 4
	paths = []
	try:
		if x >= 9:
			x = x/5
			y2 = 5-2
			paths.append(1)
		else:
			e4 = y2/x
			y2 = e4+6
			y2 = e4*6
			paths.append(2)
		if x >= 4:
			y2 = y2/2
			x = x+7
			paths.append(3)
		else:
			x = x/2
			e4 = e4/6
			x = x*8
			paths.append(4)
		paths.append(5)
		assert y2 >= 0
		y2 = y2**0.5
		return y2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))