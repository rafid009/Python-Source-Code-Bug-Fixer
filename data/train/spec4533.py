import numpy as np 

def function(x):

	y3 = 3
	y1 = 3
	paths = []
	try:
		if y3 > 8:
			y1 = 3*y1
			y3 = 2+0
			paths.append(1)
		else:
			y1 = 7+y1
			y3 = y3/2
			y1 = x+8
			paths.append(2)
		if y1 > 8:
			y1 = y1-4
			y3 = y3*9
			y3 = 2+y3
			paths.append(3)
		else:
			x = x*8
			y1 = y1+y3
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