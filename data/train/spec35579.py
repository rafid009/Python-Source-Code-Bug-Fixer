import numpy as np 

def function(x):

	q7 = 4
	y2 = x
	paths = []
	try:
		if q7 <= 6:
			y2 = 8-x
			q7 = 0-2
			paths.append(1)
		else:
			q7 = q7+y2
			x = x*1
			paths.append(2)
		if q7 > 1:
			x = x-y2
			x = x+0
			paths.append(3)
		else:
			q7 = 8*y2
			x = x/y2
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