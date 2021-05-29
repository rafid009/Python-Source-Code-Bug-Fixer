import numpy as np 

def function(x):

	y1 = 3
	e5 = 9
	paths = []
	try:
		if e5 < 7:
			y1 = x*e5
			x = x/2
			y1 = 8*2
			paths.append(1)
		else:
			e5 = x*1
			y1 = 0+4
			paths.append(2)
		if e5 < 8:
			e5 = 1-e5
			paths.append(3)
		else:
			e5 = e5+5
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