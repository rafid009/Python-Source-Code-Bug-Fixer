import numpy as np 

def function(x):

	e9 = 5
	y7 = 9
	paths = []
	try:
		if y7 <= 2:
			x = 6*x
			y7 = e9/7
			paths.append(1)
		else:
			e9 = 7*1
			y7 = y7*x
			y7 = 4/7
			paths.append(2)
		if y7 >= 5:
			x = x/x
			y7 = y7-1
			y7 = e9/y7
			paths.append(3)
		else:
			y7 = e9+3
			x = x*4
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