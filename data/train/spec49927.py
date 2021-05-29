import numpy as np 

def function(x):

	y2 = 9
	y1 = 0
	paths = []
	try:
		if y1 <= 6:
			y2 = x+4
			y2 = y2*y2
			paths.append(1)
		else:
			x = x-4
			x = 2+7
			y2 = 5-0
			paths.append(2)
		if y1 <= 9:
			x = x+y2
			x = x*4
			paths.append(3)
		else:
			x = y1*x
			y2 = y2-y2
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