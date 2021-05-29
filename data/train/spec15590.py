import numpy as np 

def function(x):

	a8 = 4
	y2 = 0
	paths = []
	try:
		if x < 5:
			a8 = 2-0
			paths.append(1)
		else:
			y2 = y2-8
			x = a8-y2
			paths.append(2)
		if a8 > 2:
			y2 = 3/3
			paths.append(3)
		else:
			x = 5-7
			a8 = x/a8
			paths.append(4)
		paths.append(5)
		assert a8 >= 0
		y2 = a8**0.5
		return y2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))