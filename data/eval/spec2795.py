import numpy as np 

def function(x):

	y2 = 2
	e1 = x
	paths = []
	try:
		if y2 >= 7:
			e1 = y2*e1
			x = x/y2
			x = x-5
			paths.append(1)
		else:
			x = x*6
			paths.append(2)
		if e1 <= 6:
			y2 = 8+1
			x = x+1
			y2 = y2*y2
			paths.append(3)
		else:
			e1 = 7-y2
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