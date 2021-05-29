import numpy as np 

def function(x):

	y5 = 0
	d8 = 7
	x = x
	paths = []
	try:
		if y5 <= 4:
			y5 = y5-2
			d8 = d8-x
			d8 = d8*y5
			paths.append(1)
		else:
			x = x-y5
			paths.append(2)
		if x >= 2:
			x = 9*x
			paths.append(3)
		else:
			x = y5-6
			paths.append(4)
		paths.append(5)
		assert y5 >= 0
		y5 = y5**0.5
		return y5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))