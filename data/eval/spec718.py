import numpy as np 

def function(x):

	a8 = 7
	y2 = 2
	paths = []
	try:
		if a8 >= 3:
			a8 = x+y2
			a8 = a8+y2
			paths.append(1)
		else:
			y2 = 4+5
			paths.append(2)
		if a8 <= 1:
			x = x-2
			a8 = a8-x
			x = x+9
			paths.append(3)
		else:
			a8 = a8*5
			x = x+a8
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