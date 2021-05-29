import numpy as np 

def function(x):

	v9 = 0
	y1 = 4
	paths = []
	try:
		if y1 > 0:
			y1 = y1/6
			y1 = 3/y1
			paths.append(1)
		else:
			x = x/y1
			y1 = 7*y1
			x = 0-4
			paths.append(2)
		if x < 0:
			x = 0-y1
			x = x-8
			y1 = x+v9
			paths.append(3)
		else:
			y1 = y1*1
			v9 = v9*0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y1 = x**0.5
		return y1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))