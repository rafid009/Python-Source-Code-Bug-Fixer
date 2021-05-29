import numpy as np 

def function(x):

	p8 = x
	y2 = x
	paths = []
	try:
		if y2 < 4:
			y2 = 3+7
			x = 0/x
			y2 = 7-4
			paths.append(1)
		else:
			p8 = p8-3
			y2 = y2/x
			paths.append(2)
		if x > 0:
			y2 = y2-2
			paths.append(3)
		else:
			p8 = y2+4
			x = x-1
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