import numpy as np 

def function(x):

	y2 = 6
	f5 = 4
	x = x
	paths = []
	try:
		if y2 > 0:
			y2 = 5-y2
			paths.append(1)
		else:
			y2 = x-y2
			y2 = 2+5
			paths.append(2)
		if f5 > 1:
			y2 = 2-y2
			y2 = y2-8
			f5 = 1/y2
			paths.append(3)
		else:
			y2 = y2*1
			y2 = 8/y2
			y2 = x*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))