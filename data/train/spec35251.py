import numpy as np 

def function(x):

	d2 = 4
	y2 = 1
	paths = []
	try:
		if x >= 4:
			d2 = d2-8
			x = y2+x
			x = 3-x
			paths.append(1)
		else:
			x = x-1
			d2 = 3+d2
			d2 = 2-d2
			paths.append(2)
		if x <= 0:
			y2 = 4+y2
			paths.append(3)
		else:
			d2 = 7+x
			d2 = d2+y2
			y2 = d2-y2
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