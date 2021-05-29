import numpy as np 

def function(x):

	e8 = 1
	y6 = 7
	paths = []
	try:
		if y6 <= 3:
			y6 = y6/x
			x = x-e8
			paths.append(1)
		else:
			e8 = e8-e8
			y6 = 9*y6
			paths.append(2)
		if y6 <= 8:
			y6 = 9*y6
			paths.append(3)
		else:
			x = y6+x
			e8 = 5-x
			paths.append(4)
		paths.append(5)
		assert e8 >= 0
		y6 = e8**0.5
		return y6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))