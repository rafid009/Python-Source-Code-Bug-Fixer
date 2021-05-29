import numpy as np 

def function(x):

	f4 = x
	y7 = 6
	paths = []
	try:
		if f4 > 8:
			y7 = y7-f4
			paths.append(1)
		else:
			f4 = 5*x
			y7 = y7*7
			paths.append(2)
		if x <= 1:
			y7 = y7/6
			x = 2+x
			y7 = x-y7
			paths.append(3)
		else:
			y7 = y7/y7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y7 = x**0.5
		return y7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))